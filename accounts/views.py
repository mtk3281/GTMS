from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from .forms import CustomUserCreationForm, UserEmailForm
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404

CustomUser = get_user_model()

def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'accounts/login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)  # Log the user out
    return redirect('home')

def email_entry_view(request):
    if request.method == 'POST':
        form = UserEmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user, created = CustomUser.objects.get_or_create(email=email)

            if not created:
                # Check if the user is active or inactive
                if user.is_active:
                    messages.warning(request, "Email already registered. Use another.")
                    return render(request, 'accounts/email_entry.html', {'form': form})  # Render the form with warning
                else:
                    # If the user is inactive, send verification email
                    messages.info(request, "A verification email has already been sent. Please check your inbox.")
                    send_verification_email(request, user)
                    return redirect('email_verification_sent')
            else:
                # Set user as inactive until verified
                user.is_active = False
                user.save()
                send_verification_email(request, user)
                return redirect('email_verification_sent')
    else:
        form = UserEmailForm()

    return render(request, 'accounts/email_entry.html', {'form': form})

def email_verification_sent_view(request):
    return render(request, 'accounts/email_verification_sent.html')


def send_verification_email(request, user):
    try:
        token = token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        domain = get_current_site(request).domain

        # Use reverse to generate the verification URL
        verification_link = reverse('email_verification', kwargs={'uidb64': uid, 'token': token})

        full_link = f"http://{domain}{verification_link}"
        print("Verification link:", full_link)

        subject = "Verify your email"
        message = render_to_string('accounts/verification_email.html', {'link': full_link})

        send_mail(subject, message, 'no-reply@yourdomain.com', [user.email])
    except Exception as e:
        print(f"Error sending email: {e}")

def verify_email_view(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        if not hasattr(user, 'profile') or user.skill_profile is None:  # Check for profile existence
            messages.success(request, 'Email verification successful! Please complete your profile.')
            return redirect('profile_creation', user_id=user.user_id)  # Use user.user_id here
        else:
            messages.success(request, 'Email verification successful! You can now log in.')
            return redirect('login')
    else:
        messages.error(request, 'Invalid verification link. Please try again.')
        return render(request, 'accounts/verification_failed.html')
    

def profile_creation_view(request, user_id):
    user = get_object_or_404(CustomUser, user_id=user_id)

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Profile updated successfully! You can now log in.')
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm(instance=user)
    
    return render(request, 'accounts/profile_creation.html', {'form': form})

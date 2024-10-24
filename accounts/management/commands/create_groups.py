from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Create default groups: Trainee, Mentor, Admin'

    def handle(self, *args, **kwargs):
        # Define the group names
        groups = ['trainee', 'mentor', 'admin']
        
        # Loop through each group name
        for group_name in groups:
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(f"Group '{group_name}' created successfully.")
            else:
                self.stdout.write(f"Group '{group_name}' already exists.")
            
            # Assign permissions to groups
            if group_name == 'admin':
                # Example: assign all permissions to 'admin'
                permissions = Permission.objects.all()
                group.permissions.set(permissions)
                self.stdout.write(f"All permissions assigned to '{group_name}'.")

            elif group_name == 'mentor':
                # Example: mentors get fewer permissions
                # Customize which permissions mentors should have
                permissions = Permission.objects.filter(codename__in=[
                    'add_task', 'change_task', 'view_task','delete_task'
                ])
                group.permissions.set(permissions)
                self.stdout.write(f"Mentor permissions assigned to '{group_name}'.")

            elif group_name == 'trainee':
                # Example: trainees only get view permissions
                permissions = Permission.objects.filter(codename__in=[
                    'view_task'
                ])
                group.permissions.set(permissions)
                self.stdout.write(f"Trainee permissions assigned to '{group_name}'.")

        self.stdout.write(self.style.SUCCESS('Groups and permissions successfully set up.'))

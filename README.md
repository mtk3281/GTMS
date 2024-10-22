# Graduate Trainee Management System (GTMS)

## Overview

The Graduate Trainee Management System (GTMS) is a centralized platform designed to manage and monitor the progress of graduate trainees. Built on AWS for scalability, GTMS focuses on user management, task management, project tracking, and performance evaluation.

## Features

### 1. User Management
- **User Roles:**
  - **Graduate Trainees:** Access tasks, projects, and track progress.
  - **Mentors/Supervisors:** Assign tasks, monitor performance, and provide feedback.
  - **Administrators:** Manage system settings, users, and reports.
- **Role-Based Access Control (RBAC):** Secure user data by managing permissions.

### 2. Task Management
- **Task Assignment:** Assign tasks with deadlines; mentors monitor and guide.
- **Collaboration:** In-app messaging for trainee-mentor communication (using Django Channels and WebSockets).
- **Workflow Management:** Kanban-style board to track task progress (To Do, In Progress, Completed).
- **Notifications:** Automated alerts for overdue tasks or task completion.

### 3. Project Management
- **Project Creation & Management:** Define projects, milestones, and assign teams based on skills.
- **Real-Time Updates:** Track project milestones and generate health reports.

### 4. Performance Evaluation
- **Metrics & KPIs:** Track key metrics like task completion rates and skill acquisition.
- **Periodic Reviews:** Schedule reviews to evaluate trainee progress, with automated report generation.
- **Trainee Profiles:** Store historical performance data for analysis.

## Technical Requirements

- **Cloud Platform:** AWS (EC2, RDS for MySQL, S3)
- **Database:** MySQL
- **Backend Framework:** Django

## Future-Proofing Considerations

### 1. Machine Learning Integration
- Predictive analytics for task completion times and project success probability.
- Skill recommendation engine based on trainee skills and career goals.
- Performance prediction to identify high-performing individuals.

### 2. API-Driven System
- REST API layer for integration with external systems and mobile apps.

### 3. Advanced Data Visualization
- Interactive dashboards for tracking progress and skill acquisition.
- Skill gap analysis visualizations.

### 4. DevOps
- CI/CD pipeline for automated testing and deployment using tools like AWS CodePipeline or GitHub Actions.

### 5. Gamification
- Points, badges, and leaderboards to motivate trainees.
- Achievement tracking for milestones and skill mastery.

### 6. Natural Language Processing (NLP)
- Analyze mentor feedback and performance reviews.
- Identify learning gaps through trainee inputs.

## Getting Started

### Prerequisites
- Python 3.12
- Django 5
- AWS Account

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mtk3281/GTMS.git
   cd GTMS
   ```

2. Install the required packages:
  ```bash
  Copy code
  pip install -r requirements.txt
  ```
3. Configure your AWS settings and database connections in the settings file.
4. Run migrations to set up the database:
  ```bash
  Copy code
  python manage.py migrate
  ```
5. Create a superuser for admin access:
  ```bash
  Copy code
  python manage.py createsuperuser
  ```
6. Start the development server:
  ```bash
  Copy code
  python manage.py runserver
  ```

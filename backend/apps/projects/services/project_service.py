# rules:
# project name can't be same
# who can create a project =>pm
# what shld be the initial status=>pending
# start_date can be of past for now (open for discussion)

from django.db import transaction
from rest_framework.exceptions import ValidationError
from apps.projects.models import Project
from apps.users.models import User
from apps.assignments.models import UserProjectAssignment

class ProjectService:
    @staticmethod
    @transaction.atomic
    def create_project(current_user,project_name,location,start_date):
            # 1. Verify if current user is in allowed roles list
        allowed_roles = {"project_manager"}
        if current_user.company_role not in allowed_roles:
            raise ValidationError("User is not allowed to create projects.")
            
            # 2. Verify if the project name is unique
        project_exists=   Project.objects.filter(project_name__iexact=project_name).exists()
        if project_exists:
            raise ValidationError("Project name already exists.")
            
            # 3. Create a project
        project = Project.objects.create(
                project_name = project_name,
                location = location,
                start_date = start_date
            )

        upa = UserProjectAssignment.objects.create(
            user_id = current_user, 
            project_id = project, 
            user_project_role = "project_manager"
        )
        return project

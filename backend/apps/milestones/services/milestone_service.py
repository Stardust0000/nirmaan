from rest_framework.exceptions import ValidationError
from apps.milestones.models import Milestone
from apps.assignments.models import UserProjectAssignment

class MilestoneService:
    def create_milestone_for_project(current_user,project,title,
    start_date, end_date):
        # 1. Find assignment using: current_user + project
        try:
            assignment = UserProjectAssignment.objects.get(
                user_id=current_user, 
                project_id=project
            )
        except UserProjectAssignment.DoesNotExist:
            raise ValidationError(
                "User is not assigned to this project."
            )
        
        # 2. Verify assignment active
        if not assignment.is_active:
            raise ValidationError("User Assignment is not active")
        
        # 3. Verify role
        allowed_roles = {"project_manager","supervisor"}
        if assignment.user_project_role not in allowed_roles:
            raise ValidationError("User is not allowed to create milestone for this project.")
        
        # 4. Create milestone
        milestone = Milestone.objects.create(
            project = project,
            title = title,
            start_date = start_date,
            end_date = end_date,
            created_by = assignment
            )
    
        # 5.Return milestone
        return milestone
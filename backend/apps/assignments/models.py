from django.db import models

class UserProjectAssignment(models.Model):

    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='upa_user_id')
    
    project_id = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name='upa_project_id')
    
    ROLE_CHOICES = [('project_manager','Project Manager'), 
                    ('supervisor','Supervisor'),
                    ('worker','Worker')]
    
    user_project_role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="worker")  

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_project_role
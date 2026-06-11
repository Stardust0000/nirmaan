from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=10, unique=True)

    COMPANY_ROLES = [
        ('project_manager', 'Project Manager'), 
        ('supervisor','Supervisor'),
        ('employee','Employee')
    ]
    company_role = models.CharField(
                        max_length=30, 
                        choices=COMPANY_ROLES, 
                        default='employee'
                    )
    
    def __str__(self):
        return self.username
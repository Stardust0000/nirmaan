from django.db import models

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=100)
    
    location = models.CharField(max_length=100)
    
    start_date = models.DateField()
    
    STATUS_CHOICES = [('pending', 'Pending'),('in_progress', 'In Progress'), ('completed','Completed'),]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return self.project_name
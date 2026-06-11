from django.db import models

# Create your models here.
class Milestone(models.Model):
 #id django can create automatically if i don't mention
   STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

 # Foreign keys:
   project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name="milestones")

   created_by = models.ForeignKey('assignments.UserProjectAssignment', on_delete=models.CASCADE, related_name="milestones_created_by_upa")

   completed_by = models.ForeignKey('assignments.UserProjectAssignment', on_delete=models.CASCADE, related_name="milestones_completed_by_upa", null=True, blank=True)

    #User defined:
   title = models.CharField(max_length=200)
   description = models.TextField(blank=True)
   order = models.PositiveIntegerField(default=0)
   status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")  


 #User defined dates
   start_date = models.DateField()
   end_date = models.DateField()

 # Automated DB timestamp  
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

  # Execution Tracking timestamp  
   completed_date = models.DateTimeField(null=True, blank=True)

   class Meta:
            # Crucial: This tells Django to ALWAYS sort queries by the 'order' field by default
      ordering = ['project','order']

   def __str__(self):
      return self.title
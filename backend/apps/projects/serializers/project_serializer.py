from rest_framework import serializers
from apps.projects.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Project
        fields = ['id','project_name','location','start_date','status']
        read_only_fields=['id']

    
    def validate_project_name(self, project_name):
        if not project_name or not project_name.strip():
            raise serializers.ValidationError("Project name cannot be empty")
        return project_name.strip()
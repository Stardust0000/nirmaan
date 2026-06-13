from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from .serializers.milestone_serializer import MilestoneSerializer
from .services.milestone_service import MilestoneService
from apps.projects.models import Project

class MilestoneView(APIView):
    #url: /api/project/<project_id>/milestones/
    def post(self, request, project_id):
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            raise ValidationError(
                "Project does not exist."
            )
        current_user = request.user

        serializer = MilestoneSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user_req = MilestoneService.create_milestone_for_project(current_user,project, validated_data = serializer.validated_data ) 
        except Exception as e: 
            return Response( {"error": str(e)}, status=status.HTTP_400_BAD_REQUEST )
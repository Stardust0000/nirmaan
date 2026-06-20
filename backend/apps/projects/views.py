from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from .serializers.project_serializer import ProjectSerializer
from .services.project_service import ProjectService
from apps.users.models import User
class ProjectView(APIView):
    # url: /api/project/
    def post(self, request):        
        current_user = request.user    
        serializer = ProjectSerializer(data = request.data)

        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        try:
            project = ProjectService.create_project(
                current_user,
                validated_data['project_name'],
                validated_data['location'],
                validated_data['start_date']
            )
            return Response({"success":project.project_name}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)


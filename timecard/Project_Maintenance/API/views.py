from Project_Maintenance.models import ProjectMaintenance
from django.http import JsonResponse
from rest_framework.response import Response
from Project_Maintenance.API.serializer import ProjectSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated



def json_project_list(request):
    project = ProjectMaintenance.objects.all()
    all_projects = {"Project": list(project.values())}
    return JsonResponse(all_projects)

@api_view(['GET', 'PUT', 'DELETE'])
def api_project_detail(request, pk):
    labor_found = ProjectMaintenance.objects.filter(pk=pk).count()
    if not labor_found:
        return Response(status=status.HTTP_404_NOT_FOUND)
    project = ProjectMaintenance.objects.get(pk=pk)
    if request.method == 'GET':
        serialized_course = ProjectSerializer(project)
        return Response(serialized_course.data)
    elif request.method == 'PUT':
        serialized_course = ProjectSerializer(project, data=request.data)
        if serialized_course.is_valid():
            serialized_course.save()
            return Response(serialized_course.data)
        return Response(serialized_course.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        project.delete()
        return Response({'message': f'Course {project.name} deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

class ProjectList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        project = ProjectMaintenance.objects.all()
        serialized_project = ProjectSerializer(project, many=True)
        return Response(serialized_project.data)

    def post(self, request):
        serialized_project = ProjectSerializer(data=request.data)
        if serialized_project.is_valid():
            serialized_project.save()
            return Response(serialized_project.data, status=status.HTTP_201_CREATED)
        return Response(serialized_project.errors, status=status.HTTP_400_BAD_REQUEST)
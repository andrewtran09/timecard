from labor_code_maintenance.models import LaborCodeMaintenance
from django.http import JsonResponse
from rest_framework.response import Response
from labor_code_maintenance.API.serializer import LaborSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated



def json_labor_list(request):
    labor = LaborCodeMaintenance.manager.all()
    all_labor = {"Labors": list(labor.values())}
    return JsonResponse(all_labor)

@api_view(['GET', 'PUT', 'DELETE'])
def api_labor_detail(request, pk):
    labor_found = LaborCodeMaintenance.manager.filter(pk=pk).count()
    if not labor_found:
        return Response(status=status.HTTP_404_NOT_FOUND)
    labor = LaborCodeMaintenance.manager.get(pk=pk)
    if request.method == 'GET':
        serialized_course = LaborSerializer(labor)
        return Response(serialized_course.data)
    elif request.method == 'PUT':
        serialized_course = LaborSerializer(labor, data=request.data)
        if serialized_course.is_valid():
            serialized_course.save()
            return Response(serialized_course.data)
        return Response(serialized_course.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        labor.delete()
        return Response({'message': f'Course {labor.name} deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

class LaborList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        labor = LaborCodeMaintenance.manager.all()
        serialized_labor = LaborSerializer(labor, many=True)
        return Response(serialized_labor.data)

    def post(self, request):
        serialized_post = LaborSerializer(data=request.data)
        if serialized_post.is_valid():
            serialized_post.save()
            return Response(serialized_post.data, status=status.HTTP_201_CREATED)
        return Response(serialized_post.errors, status=status.HTTP_400_BAD_REQUEST)
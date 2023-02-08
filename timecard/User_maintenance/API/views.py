from rest_framework.response import Response
from .serializer import *
from rest_framework.decorators import api_view
from ..models import *
from  rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


@api_view(['GET','PUT','DELETE'])
def userrole(request,pk):
    user1 = UserRole.objects.filter(pk=pk).count
    if not user1:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = UserRole.objects.filter(pk=pk)
    if request.method == 'GET':
        serialized_user = UserRoleserializer(user, many= True)
        return Response(serialized_user.data)
    elif request.method == "POST":
        serialized_user = UserRoleserializer(data=request.data)
        if serialized_user.is_valid():
            serialized_user.save()
            return Response(serialized_user.data)
        return Response(serialized_user.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
            user.delete()
            return Response({'message': f'Course {user.name} deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


class RoleList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = UserRole.objects.all()
        serialized_user = UserRoleserializer(user, many=True)
        return Response (serialized_user.data)

    def post(self,request):
        serialized_post = UserRoleserializer(data=request.data)
        if serialized_post.is_valid():
            serialized_post.save()
            return Response(serialized_post.data,status=status.HTTP_201_CREATED)
        return Response(serialized_post.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def usermain(request,pk):
    user1 = UserMaintenance.objects.filter(pk=pk).count
    if not user1:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = UserMaintenance.objects.filter(pk=pk)
    if request.method == 'GET':
        serialized_user = UserMaintenanceserilaizer(user, many= True)
        return Response(serialized_user.data)
    elif request.method == "POST":
        serialized_user = UserMaintenanceserilaizer(data=request.data)
        if serialized_user.is_valid():
            serialized_user.save()
            return Response(serialized_user.data)
        return Response(serialized_user.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
            user.delete()
            return Response({'message': f'Course {user.name} deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


class MaintList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = UserMaintenance.objects.all()
        serialized_user = UserMaintenanceserilaizer(user, many=True)
        return Response (serialized_user.data)

    def post(self,request):
        serialized_post = UserMaintenanceserilaizer(data=request.data)
        if serialized_post.is_valid():
            serialized_post.save()
            return Response(serialized_post.data,status=status.HTTP_201_CREATED)
        return Response(serialized_post.errors,status=status.HTTP_400_BAD_REQUEST)

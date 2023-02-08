from ..models import TimeCardStatus, TimeCardDetails, TimeCardSubmission
from django.http import JsonResponse
from rest_framework.response import Response
from .serializer import TimeCardSerializer, TimeCardDetailSerializer, TimeCardStatusSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated



def json_TimeCardSub_list(request):
    TCS = TimeCardSubmission.manager.all()
    all_TimeCards = {"TimeCardSubmission": list(TCS.values())}
    return JsonResponse(all_TimeCards)

@api_view(['GET', 'PUT', 'DELETE'])
def api_time_card_detail(request, pk):
    time_card_found = TimeCardSubmission.manager.filter(pk=pk).count()
    if not time_card_found:
        return Response(status=status.HTTP_404_NOT_FOUND)
    time_card = TimeCardSubmission.manager.get(pk=pk)
    if request.method == 'GET':
        serialized_course = TimeCardSerializer(time_card)
        return Response(serialized_course.data)
    elif request.method == 'PUT':
        serialized_course = TimeCardSerializer(time_card, data=request.data)
        if serialized_course.is_valid():
            serialized_course.save()
            return Response(serialized_course.data)
        return Response(serialized_course.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        temp = time_card.time_card_id
        time_card.delete()
        return Response({'message': f'TimeCard {temp} deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

class Time_Card_List(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        project = TimeCardSubmission.manager.all()
        serialized_project = TimeCardSerializer(project, many=True)
        return Response(serialized_project.data)

    def post(self, request):
        serialized_time_card = TimeCardSerializer(data=request.data)
        if serialized_time_card.is_valid():
            serialized_time_card.save()
            return Response(serialized_time_card.data, status=status.HTTP_201_CREATED)
        return Response(serialized_time_card.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def api_time_card_details_detail(request, pk):
    time_card_detail_found = TimeCardDetails.manager.filter(pk=pk).count()
    if not time_card_detail_found:
        return Response(status=status.HTTP_404_NOT_FOUND)
    time_card_details = TimeCardDetails.manager.get(pk=pk)
    if request.method == 'GET':
        serialized_course = TimeCardDetailSerializer(time_card_details)
        return Response(serialized_course.data)
    elif request.method == 'PUT':
        serialized_course = TimeCardDetailSerializer(time_card_details, data=request.data)
        if serialized_course.is_valid():
            serialized_course.save()
            return Response(serialized_course.data)
        return Response(serialized_course.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        temp = time_card_details.time_card_detail_id
        time_card_details.delete()
        return Response({'message': f'TimeCard {temp} deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

class Time_Card_Detail_List(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        project = TimeCardDetails.manager.all()
        serialized_tcd = TimeCardDetailSerializer(project, many=True)
        return Response(serialized_tcd.data)

    def post(self, request):
        serialized_time_card_detail = TimeCardDetailSerializer(data=request.data)
        if serialized_time_card_detail.is_valid():
            serialized_time_card_detail.save()
            return Response(serialized_time_card_detail.data, status=status.HTTP_201_CREATED)
        return Response(serialized_time_card_detail.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def api_time_card_status_detail(request, pk):
    time_card_status_found = TimeCardStatus.manager.filter(pk=pk).count()
    if not time_card_status_found:
        return Response(status=status.HTTP_404_NOT_FOUND)
    time_card_status = TimeCardStatus.manager.get(pk=pk)
    if request.method == 'GET':
        serialized_course = TimeCardStatusSerializer(time_card_status)
        return Response(serialized_course.data)
    elif request.method == 'PUT':
        serialized_course = TimeCardStatusSerializer(time_card_status, data=request.data)
        if serialized_course.is_valid():
            serialized_course.save()
            return Response(serialized_course.data)
        return Response(serialized_course.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        temp = time_card_status.status_id
        time_card_status.delete()
        return Response({'message': f'TimeCard {temp} deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

class Time_Card_Status_List(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        project = TimeCardStatus.manager.all()
        serialized_tcs = TimeCardStatusSerializer(project, many=True)
        return Response(serialized_tcs.data)

    def post(self, request):
        serialized_time_card_status = TimeCardStatusSerializer(data=request.data)
        if serialized_time_card_status.is_valid():
            serialized_time_card_status.save()
            return Response(serialized_time_card_status.data, status=status.HTTP_201_CREATED)
        return Response(serialized_time_card_status.errors, status=status.HTTP_400_BAD_REQUEST)
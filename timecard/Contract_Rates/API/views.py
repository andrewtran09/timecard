from rest_framework.response import Response
from .serializer import *
from rest_framework.decorators import api_view
from ..models import ContractRatesHeader,RateUnit,ContractRatesDetails,ContractRateTransmit
from  rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

@api_view(['GET','PUT','DELETE'])
def contract_header(request,pk):
    contr1 = ContractRatesHeader.object.filter(pk=pk).count
    if not contr1:
        return Response(status=status.HTTP_404_NOT_FOUND)

    contr = ContractRatesHeader.object.filter(pk=pk)
    if request.method == 'GET':
        serialized_contr = ContractRatesHeaderserializer(contr, many= True)
        return Response(serialized_contr.data)
    elif request.method == "POST":
        serialized_contr = ContractRatesHeaderserializer(data=request.data)
        if serialized_contr.is_valid():
            serialized_contr.save()
            return Response(serialized_contr.data)
        return Response(serialized_contr.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
            contr.delete()
            return Response({'message': f'Course {contr.name} deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


class HeaderList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        contr = ContractRatesHeader.object.all()
        serialized_contr = ContractRatesHeaderserializer(contr, many=True)
        return Response (serialized_contr.data)

    def post(self,request):
        serialized_post = ContractRatesHeaderserializer(data=request.data)
        if serialized_post.is_valid():
            serialized_post.save()
            return Response(serialized_post.data,status=status.HTTP_201_CREATED)
        return Response(serialized_post.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def contract_unit(request,pk):
    rate_unit = RateUnit.object.filter(pk=pk).count()
    if not rate_unit:
        return Response(status=status.HTTP_404_NOT_FOUND)

    rateu = RateUnit.object.filter(pk=pk)
    if request.method == 'GET':
        serialized_rateu = RateUnitserializer(rateu, many= True)
        return Response(serialized_rateu.data)
    elif request.method == "POST":
        serialized_rateu = RateUnitserializer(data=request.data)
        if serialized_rateu.is_valid():
            serialized_rateu.save()
            return Response(serialized_rateu.data)
        return Response(serialized_rateu.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
            rateu.delete()
            return Response({'message': f'Course {rateu.name} deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

class UnitList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        rateu = RateUnit.object.all()
        serialized_rateu = RateUnitserializer(rateu, many=True)
        return Response (serialized_rateu.data)

    def post(self,request):
        serialized_post = RateUnitserializer(data=request.data)
        if serialized_post.is_valid():
            serialized_post.save()
            return Response(serialized_post.data,status=status.HTTP_201_CREATED)
        return Response(serialized_post.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def contract_details(request,pk):
    det_list = ContractRatesDetails.object.filter(pk=pk).count()
    if not det_list:
        return Response(status=status.HTTP_404_NOT_FOUND)

    detail = ContractRatesDetails.object.filter(pk=pk)
    if request.method == 'GET':
        serialized_detail = ContractRatesDetailsserializer(detail, many= True)
        return Response(serialized_detail.data)
    elif request.method == "POST":
        serialized_detail = ContractRatesDetailsserializer(data=request.data)
        if serialized_detail.is_valid():
            serialized_detail.save()
            return Response(serialized_detail.data)
        return Response(serialized_detail.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        detail.delete()
        return Response({'message': f'Course {detail.name} deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


class DetailList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        detail = ContractRatesDetails.object.all()
        serialized_detail = ContractRatesDetailsserializer(detail, many=True)
        return Response (serialized_detail.data)

    def post(self,request):
        serialized_post = ContractRatesDetailsserializer(data=request.data)
        if serialized_post.is_valid():
            serialized_post.save()
            return Response(serialized_post.data,status=status.HTTP_201_CREATED)
        return Response(serialized_post.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def contract_transmit(request,pk):
    trans_list = ContractRateTransmit.object.filter(pk=pk).count()
    if not trans_list:
        return Response(status=status.HTTP_404_NOT_FOUND)

    trans = ContractRateTransmit.object.filter(pk=pk)
    if request.method == 'GET':
        serialized_trans = ContractRateTransmitserializer(trans, many= True)
        return Response(serialized_trans.data)
    elif request.method == "POST":
        serialized_trans = ContractRateTransmitserializer(data=request.data)
        if serialized_trans.is_valid():
            serialized_trans.save()
            return Response(serialized_trans.data)
        return Response(serialized_trans.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        trans.delete()
        return Response({'message': f'Course {trans.name} deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

class TransList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        trans = ContractRateTransmit.object.all()
        serialized_trans = ContractRateTransmitserializer(trans, many=True)
        return Response (serialized_trans.data)

    def post(self,request):
        serialized_post = ContractRateTransmitserializer(data=request.data)
        if serialized_post.is_valid():
            serialized_post.save()
            return Response(serialized_post.data,status=status.HTTP_201_CREATED)
        return Response(serialized_post.errors,status=status.HTTP_400_BAD_REQUEST)

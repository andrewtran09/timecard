from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import SuppliesCodeMaintenanceSerializer
from supplies_code_maintenance.models import SuppliesCodeMaintenance


@api_view(['GET', 'POST'])
def sc_list(request):
    if request.method == 'GET':
        sc = SuppliesCodeMaintenance.manager.all()
        serialized_sc = SuppliesCodeMaintenanceSerializer(sc, many=True)
        return Response(serialized_sc.data)
    elif request.method == "POST":
        serialized_sc = SuppliesCodeMaintenanceSerializer(data=request.data)
        if serialized_sc.is_valid():
            serialized_sc.save()
            return Response(serialized_sc.data)
        else:
            return Response(serialized_sc.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def sc_list_detail(request, pk):
    sc_found = SuppliesCodeMaintenance.manager.filter(pk=pk).count()

    if not sc_found:
        return Response(status=status.HTTP_404_NOT_FOUND)

    sc = SuppliesCodeMaintenance.manager.get(pk=pk)

    if request.method == 'GET':
        serialized_sc = SuppliesCodeMaintenanceSerializer(sc)
        return Response(serialized_sc.data)
    elif request.method == 'PUT':
        serialized_sc = SuppliesCodeMaintenanceSerializer(sc, data=request.data)

        if serialized_sc.is_valid():
            serialized_sc.save()
            return Response(serialized_sc.data)
        else:
            return Response(serialized_sc.errors)
    elif request.method == 'DELETE':
        sc.delete()
        return Response({'message': f'Supplies Code {sc.sc_desc} deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
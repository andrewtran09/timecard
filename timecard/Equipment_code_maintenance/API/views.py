from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import EquipmentCodeMaintenanceSerializer
from Equipment_code_maintenance.models import EquipmentCodeMaintenance


@api_view(['GET', 'POST'])
def ecm_list(request):
    if request.method == 'GET':
        ecm = EquipmentCodeMaintenance.object.all()
        serialized_ecm = EquipmentCodeMaintenanceSerializer(ecm, many=True)
        return Response(serialized_ecm.data)
    elif request.method == "POST":
        serialized_ecm = EquipmentCodeMaintenanceSerializer(data=request.data)
        if serialized_ecm.is_valid():
            serialized_ecm.save()
            return Response(serialized_ecm.data)
        else:
            return Response(serialized_ecm.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def ecm_list_detail(request, pk):
    ecm_found = EquipmentCodeMaintenance.object.filter(pk=pk).count()

    if not ecm_found:
        return Response(status=status.HTTP_404_NOT_FOUND)

    ecm = EquipmentCodeMaintenance.object.get(pk=pk)

    if request.method == 'GET':
        serialized_ecm = EquipmentCodeMaintenanceSerializer(ecm)
        return Response(serialized_ecm.data)
    elif request.method == 'PUT':
        serialized_ecm = EquipmentCodeMaintenanceSerializer(ecm, data=request.data)

        if serialized_ecm.is_valid():
            serialized_ecm.save()
            return Response(serialized_ecm.data)
        else:
            return Response(serialized_ecm.errors)
    elif request.method == 'DELETE':
        ecm.delete()
        return Response({'message': f'Equipment Code {ecm.equipment_code} deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
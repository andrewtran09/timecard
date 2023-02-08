from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import ProjectExpenseCodeMaintenanceSerializer
from Project_expense_code_maintenance.models import ProjectExpenseCodeMaintenance


@api_view(['GET', 'POST'])
def expense_list(request):
    if request.method == 'GET':
        expense = ProjectExpenseCodeMaintenance.object.all()
        serialized_expense = ProjectExpenseCodeMaintenanceSerializer(expense, many=True)
        return Response(serialized_expense.data)
    elif request.method == "POST":
        serialized_expense = ProjectExpenseCodeMaintenanceSerializer(data=request.data)
        if serialized_expense.is_valid():
            serialized_expense.save()
            return Response(serialized_expense.data)
        else:
            return Response(serialized_expense.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def expense_list_detail(request, pk):
    expense_found = ProjectExpenseCodeMaintenance.object.filter(pk=pk).count()

    if not expense_found:
        return Response(status=status.HTTP_404_NOT_FOUND)

    expense = ProjectExpenseCodeMaintenance.object.get(pk=pk)

    if request.method == 'GET':
        serialized_expense = ProjectExpenseCodeMaintenanceSerializer(expense)
        return Response(serialized_expense.data)
    elif request.method == 'PUT':
        serialized_expense = ProjectExpenseCodeMaintenanceSerializer(expense, data=request.data)

        if serialized_expense.is_valid():
            serialized_expense.save()
            return Response(serialized_expense.data)
        else:
            return Response(serialized_expense.errors)
    elif request.method == 'DELETE':
        expense.delete()
        return Response({'message': f'Equipment Code {expense.expense_code} deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
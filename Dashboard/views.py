from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Transactions
from .serializers import TransactionSerializer


@api_view(['GET'])
def get_transaction(request):
    transactions = Transactions.objects.all()
    serializer = TransactionSerializer(transactions, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def create_transaction(request):
    print(request.data)
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        transaction = Transactions.objects.create(**serializer.data)
        return Response({"status": "ok", "id": transaction.id}, status=status.HTTP_201_CREATED)

    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def transaction_details(request, tran_id):
    try:
        transaction = Transactions.objects.get(id=tran_id)
    except Transactions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TransactionSerializer(transaction)
    return Response(serializer.data, status=status.HTTP_200_OK)

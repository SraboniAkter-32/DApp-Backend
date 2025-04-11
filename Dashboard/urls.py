from django.urls import path
from .views import get_transaction, create_transaction, transaction_details


urlpatterns = [
    path("transactions/", get_transaction, name="get_transaction"),
    path("transaction/create/", create_transaction, name='create_transaction'),
    path("transaction/<int:tran_id>", transaction_details, name='transaction_details'),
]

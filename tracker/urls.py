from django.urls import path
from . import views

urlpatterns = [
    path('delete-transaction/<id>', views.delete , name= "delete_transaction"),
    path('', views.index, name = "index")
]

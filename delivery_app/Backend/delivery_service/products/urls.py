from django.urls import path
from .views import *;

urlpatterns=[
    path('addCategory/',CategoryAdd.as_view()),
    path('getCategory/',getCategory.as_view()),
    path('updateCategory/<int:id>/',CategoryAdd.as_view()),
    path('deleteCategory/<int:id>/',CategoryAdd.as_view()),
    path('addProcuct/',addProduct.as_view()),
    path('getProduct/',getProduct.as_view()),
    path('updateProcuct/<int:id>/',addProduct.as_view()),
    path('deleteProcuct/<int:id>/',addProduct.as_view()),
]
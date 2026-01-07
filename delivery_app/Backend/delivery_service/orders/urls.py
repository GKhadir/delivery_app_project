from django.urls import path
from .views import *;

urlpatterns=[
    path('addOrder/',CreateOrder.as_view()),
    path('addItem/',addOrderItem.as_view()),
]
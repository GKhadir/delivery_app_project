from django.urls import path
from .views import registerApi

urlpatterns=[
    path('register/',registerApi.as_view()),
]
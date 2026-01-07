from django.shortcuts import render
from .models import *;
from users.models import *;
from products.models import *;
from .serializers import *;
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,IsAuthenticated
# Create your views here.

class CreateOrder(APIView):
    def post(self,request):
        try:
            data=request.data
            customer=UsersData.objects.get(email=request.user)
            address=addresses.objects.get(user_id=customer.id)
            data['customer_id']=customer.id
            data['address_id']=address.id
            serializer=OrderSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except UsersData.DoesNotExist:
            return Response("user not found",status=status.HTTP_404_NOT_FOUND)
        
class addOrderItem(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=OrderItemSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response("product not found",status=status.HTTP_404_NOT_FOUND)


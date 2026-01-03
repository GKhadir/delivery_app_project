from django.shortcuts import render
from .models import addresses,user_profiles,UsersData,delivary_partner_details
from .serilazers import addressesSerializer,delivary_partner_detailsSerializer,UsersDataSerializer,user_profilesSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password

# Create your views here.
class registerApi(APIView):
    def post(self,request):
        data=request.data
        serializer=UsersDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

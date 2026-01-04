from django.shortcuts import render
from .models import addresses,user_profiles,UsersData,delivary_partner_details
from .serilazers import addressesSerializer,delivary_partner_detailsSerializer,UsersDataSerializer,user_profilesSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAdminUser,IsAuthenticated

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
class AdminCurd(APIView):
    permission_classes=[IsAdminUser]
    def get(self,request):
        data=UsersData.objects.all()
        serializer=UsersDataSerializer(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def delete(self,request,email):
        try:
            data=UsersData.objects.get(email=email)
            data.delete()
            return Response("user deleted successfully..",status=status.HTTP_204_NO_CONTENT)
        except UsersData.DoesNotExist:
            return Response("user not exites..",status=status.HTTP_404_NOT_FOUND)
    
    def patch(self,request,email):
        try:
            data=UsersData.objects.get(email=email)
            print(request.data)
            serializer=UsersDataSerializer(data,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except UsersData.DoesNotExist:
            return Response("user not found",status=status.HTTP_404_NOT_FOUND)
        
class login(APIView):
    def post(self,request):
        try:
            user=UsersData.objects.get(email=request.data['email'])
            if check_password(request.data['password'],user.password):
                refresh=RefreshToken.for_user(user)
                serializer=UsersDataSerializer(user)
                return Response({
                    'user':serializer.data,
                    'access':str(refresh.access_token),
                    'refresh':str(refresh)
                },status=status.HTTP_200_OK)
            else:
                return Response("worng password or email",status=status.HTTP_400_BAD_REQUEST)
        except UsersData.DoesNotExist:
            return Response("user not exites..",status=status.HTTP_404_NOT_FOUND)
        
    def get(self,request):
        print(request.user)
        return Response("",status=status.HTTP_200_OK)
    
class createProfile(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        try:
            user=UsersData.objects.get(email=request.user)
            data=request.data
            data['user_id']=user.id
            serializer=user_profilesSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except UsersData.DoesNotExist:
            return Response("user not exites..",status=status.HTTP_404_NOT_FOUND)
    
    def patch(self,request):
        try:
            data=UsersData.objects.get(email=request.user)
            profil=user_profiles.objects.get(user_id=data.id)
            serializer=user_profilesSerializer(profil,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except UsersData.DoesNotExist:
            return Response("user not found",status=status.HTTP_404_NOT_FOUND)
        
    def get(self,request):
        data=UsersData.objects.get(email=request.user)
        profile=user_profiles.objects.get(user_id=data.id)
        serializer=user_profilesSerializer(data)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
class addAddress(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        try:
            user=UsersData.objects.get(email=request.user)
            data=request.data
            data['user_id']=user.id
            serializer=addressesSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except UsersData.DoesNotExist:
            return Response("user not found",status=status.HTTP_404_NOT_FOUND)
        
    def patch(self,request,id):
        try:
            address=addresses.objects.get(id=id)
            serializer=addressesSerializer(address,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except UsersData.DoesNotExist:
            return Response("user not found",status=status.HTTP_404_NOT_FOUND)
        
    def get(self,request):
        data=UsersData.objects.get(email=request.user)
        address=addresses.objects.filter(user_id=data.id)
        serializer=addressesSerializer(address,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def delete(self,request,id):
        try:
            data=addresses.objects.get(id=id)
            data.delete()
            return Response("address deleted successfully..",status=status.HTTP_204_NO_CONTENT)
        except UsersData.DoesNotExist:
            return Response("address not exites..",status=status.HTTP_404_NOT_FOUND)
        
class createdelivary_partner(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        try:
            user=UsersData.objects.get(email=request.user)
            if user.role=='delivery':
                data=request.data
                data['user_id']=user.id
                serializer=delivary_partner_detailsSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response("only delivery partner can create",status=status.HTTP_401_UNAUTHORIZED)
        except UsersData.DoesNotExist:
            return Response("user not exites..",status=status.HTTP_404_NOT_FOUND)
    
    def patch(self,request):
        try:
            data=UsersData.objects.get(email=request.user)
            partner=delivary_partner_details.objects.get(user_id=data.id)
            serializer=delivary_partner_detailsSerializer(partner,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except UsersData.DoesNotExist:
            return Response("user not found",status=status.HTTP_404_NOT_FOUND)
        
    def get(self,request):
        data=UsersData.objects.get(email=request.user)
        partenr=delivary_partner_details.objects.get(user_id=data.id)
        serializer=delivary_partner_detailsSerializer(partenr)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
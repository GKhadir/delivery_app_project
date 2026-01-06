from .models import *;
from .serilazer import *;
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
class CategoryAdd(APIView):
    def post(self,request):
        data=request.data
        serializer=CategorySerilazer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self,request,id):
        try:
            data=Category.objects.get(id=id)
            serializer=CategorySerilazer(data,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Category.DoesNotExist:
            return Response("product not found",status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,request,id):
        try:
            data=Category.objects.get(id=id)
            data.delete()
            return Response("delete successfully...",status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response("product not found",status=status.HTTP_404_NOT_FOUND)   
    
class getCategory(APIView):
    def get(self,request):
        data=Category.objects.all()
        serializer=CategorySerilazer(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class addProduct(APIView):
    def post(self,request):
        data=request.data
        serializer=ProductSerilazer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self,request,id):
        try:
            data=Product.objects.get(id=id)
            serializer=ProductSerilazer(data,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response("product not found",status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,request,id):
        try:
            data=Product.objects.get(id=id)
            data.delete()
            return Response("delete successfully...",status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response("product not found",status=status.HTTP_404_NOT_FOUND)

class getProduct(APIView):
    def get(self,request):
        data=Product.objects.all()
        serializer=ProductSerilazer(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
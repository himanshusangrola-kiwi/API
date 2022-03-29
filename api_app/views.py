from functools import partial
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartItemSerializers
from .models import CartItem
from rest_framework import viewsets

class CartItemViewSet(viewsets.ViewSet):
    def list(self, request):
        """function to list all objects"""
        cartitem=CartItem.objects.all()
        serializer=CartItemSerializers(cartitem, many=True)
        return Response(serializer.data)

    def retrive(self, request, pk=None):
        """function to list a single object"""
        cartitem=CartItem.objects.get(id=pk)
        serializer=CartItemSerializers(cartitem)
        return Response(serializer.data)

    def create(self, request):
        """function to create a object"""
        serializer=CartItemSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        """function to update a object"""
        cartitem = CartItem.objects.get(id=pk)
        serializer = CartItemSerializers(cartitem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request,pk):
        """function to update a object partially"""
        cartitem = CartItem.objects.get(id=pk)
        serializer = CartItemSerializers(cartitem, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Partially Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        """function to Delete the object"""
        cartitem = CartItem.objects.get(id=pk)
        cartitem.delete()
        return Response({'msg':'Data Deleted'})

        

# class CartItemViews(APIView):
#     def post(self, request):
#         """A View to Create a Object of CartItem Model"""
#         serializer=CartItemSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status":"success","data": serializer.data}, status=status.HTTP_200_OK)
#         else:
#             return Response({"status":"error","data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request, id=None):
#         """A View to List a particular object(by ID) or All the objects"""
#         if id:
#             item = CartItem.objects.get(id=id)
#             serializer = CartItemSerializers(item)
#             return Response({"status":"success","data": serializer.data}, status=status.HTTP_200_OK)
        
#         item = CartItem.objects.all()
#         serializer = CartItemSerializers(item, many=True)
#         return Response({"status":"success","data": serializer.data}, status=status.HTTP_200_OK)

#     def patch(self,request, id=None):
#         """A View to Update the CartItem Objects"""
#         item = CartItem.objects.get(id=id)
#         serializer = CartItemSerializers(item, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status":"success","data": serializer.data})
#         else:
#             return Response({"status":"error","data": serializer.errors})
        
#     def delete(self,request, id=None):
#         item = get_object_or_404(CartItem, id=id)
#         item.delete()
#         return Response({"status":"success" , "data": "Item Deleted"})

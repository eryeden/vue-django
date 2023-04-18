from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class SampleAPIView(APIView):
    def get(self, request):
        return Response({"message": "Hello World!"}, status=status.HTTP_200_OK)
    
    def post(self, request):
        return Response({"message": "Hello World!"}, status=status.HTTP_200_OK)
    
    def put(self, request):
        return Response({"message": "Hello World!"}, status=status.HTTP_200_OK)
    
    def delete(self, request):
        return Response({"message": "Hello World!"}, status=status.HTTP_200_OK)
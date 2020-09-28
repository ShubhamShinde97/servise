from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from .models import ServiseProvide,Clients
from django.http import Http404
from rest_framework import status

# Create your views here.
class ServiceProviders(APIView):
    def get(self, request, *args, **kwargs):
        ServicePro = ServiseProvide.objects.all()
        serializer = serializers.ServiceProviderSerializer(ServicePro, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.ServiceProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class client(APIView):
    def get(self, request):

        try:

            serviseprovider = ServiseProvide.objects.get()

        except ServiseProvide.DoesNotExist:

            raise Http404

        serializer = serializers.ServiceProviderSerializer(serviseprovider)

        return Response(serializer.data)
    '<input type="submit" value="contact" class=btn btn-success>'





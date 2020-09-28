from rest_framework import serializers
from . import models
import base64
from django.conf import settings
import os

class ServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiseProvide
        fields = ['id','name', 'post', 'phone']



class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Clients
        fields = ['id' ,'name','email']
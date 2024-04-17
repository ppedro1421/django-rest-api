from rest_framework import serializers
from .models import *


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        client = Client()
        client.name = validated_data.get('name')
        client.cnpj = validated_data.get('cnpj')
        client.save()
        return validated_data

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.cnpj = validated_data.get('cnpj', instance.cnpj)
        instance.save()
        return instance

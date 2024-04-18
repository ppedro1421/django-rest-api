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
        instance.save()
        return instance


class ClientEmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientEmployee
        fields = '__all__'

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        employee = ClientEmployee()
        employee.employer = Client.objects.get(pk=validated_data.get('employer'))
        employee.first_name = validated_data.get('first_name')
        employee.last_name = validated_data.get('last_name')
        employee.cpf = validated_data.get('cpf')
        employee.role = validated_data.get('role')
        employee.salary = validated_data.get('salary')
        employee.save()
        return validated_data

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.role = validated_data.get('role', instance.role)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.save()
        return instance

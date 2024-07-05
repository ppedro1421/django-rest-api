from rest_framework import serializers
from .models import *


class EmployerSerializer(serializers.ModelSerializer):

    class EmployeeSerializer(serializers.ModelSerializer):
        role = serializers.CharField(source='role.description', read_only=True)

        class Meta:
            model = Employee
            exclude = ['employer']

    employees = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Employer
        fields = '__all__'

    def validate(self, attrs: dict):
        return attrs

    def create(self, validated_data: dict):
        employer = Employer()
        employer.name = validated_data.get('name')
        employer.save()
        return employer

    def update(self, instance: Employer, validated_data: dict):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class RoleSerializer(serializers.ModelSerializer):
    employer = serializers.CharField(source='employer.name', read_only=True)

    class Meta:
        model = Role
        fields = '__all__'

    def validate(self, attrs: dict):
        return attrs

    def create(self, validated_data: dict):
        role = Role()
        role.employer = validated_data.get('employer')
        role.description = validated_data.get('description')
        role.save()
        return role

    def update(self, instance: Role, validated_data: dict):
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

    def validate(self, attrs: dict):
        return attrs

    def create(self, validated_data: dict):
        employee = Employee()
        employee.employer = validated_data.get('employer')
        employee.first_name = validated_data.get('first_name')
        employee.last_name = validated_data.get('last_name')
        employee.role = validated_data.get('role')
        employee.salary = validated_data.get('salary')
        employee.save()
        return employee

    def update(self, instance: Employee, validated_data: dict):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.role = validated_data.get('role', instance.role)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.save()
        return instance

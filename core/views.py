from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from django.db.models import Q
from .models import *
from .serializers import *


# EMPLOYER
@api_view(['GET'])
@renderer_classes([JSONRenderer, XMLRenderer])
@permission_classes([AllowAny])
def list_employer(request: Request) -> Response:
    employers = Employer.objects
    serializer = EmployerSerializer(employers, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@renderer_classes([JSONRenderer, XMLRenderer])
@permission_classes([AllowAny])
def detail_employer(request: Request, pk: int) -> Response:
    employer = Employer.objects.filter(pk=pk)
    if not employer.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = EmployerSerializer(employer.first(), many=False)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@renderer_classes([JSONRenderer, XMLRenderer])
@permission_classes([AllowAny])
def create_employer(request: Request) -> Response:
    serializer = EmployerSerializer(data=request.data)
    if not serializer.is_valid(raise_exception=True):
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer.create(serializer.data)
    return Response(status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@renderer_classes([JSONRenderer, XMLRenderer])
@permission_classes([AllowAny])
def delete_employer(request: Request, pk: int) -> Response:
    employer = Employer.objects.filter(pk=pk)
    if not employer.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    employer.delete()
    return Response(status=status.HTTP_200_OK)


# ROLE
@api_view(['GET'])
@renderer_classes([JSONRenderer, XMLRenderer])
@permission_classes([AllowAny])
def list_role(request: Request) -> Response:
    employer_query = request.query_params.get('employer')

    q = Q()
    if employer_query:
        q &= Q(employer=employer_query)

    roles = Role.objects.filter(q)
    serializer = RoleSerializer(roles, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@renderer_classes([JSONRenderer, XMLRenderer])
@permission_classes([AllowAny])
def create_role(request: Request) -> Response:
    serializer = RoleSerializer(data=request.data)
    if not serializer.is_valid(raise_exception=True):
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer.create(serializer.data)
    return Response(status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@renderer_classes([JSONRenderer, XMLRenderer])
@permission_classes([AllowAny])
def delete_role(request: Request, pk: int) -> Response:
    role = Role.objects.filter(pk=pk)
    if not role.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    role.delete()
    return Response(status=status.HTTP_200_OK)


# EMPLOYEE
@api_view(['GET'])
@renderer_classes([JSONRenderer, XMLRenderer])
@permission_classes([AllowAny])
def list_employee(request: Request) -> Response:
    first_name_query = request.query_params.get('first_name')
    last_name_query = request.query_params.get('last_name')
    employer_query = request.query_params.get('employer')
    role_query = request.query_params.get('role')

    q = Q()
    if first_name_query:
        q &= Q(first_name=first_name_query)
    if last_name_query:
        q &= Q(last_name=last_name_query)
    if employer_query:
        q &= Q(employer__name=employer_query)
    if role_query:
        q &= Q(role__description=role_query)

    employee = Employee.objects.filter(q)
    serializer = EmployeeSerializer(employee, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@renderer_classes([JSONRenderer, XMLRenderer])
@permission_classes([AllowAny])
def detail_employee(request: Request, pk: int) -> Response:
    employee = Employee.objects.filter(pk=pk)
    if not employee.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = EmployeeSerializer(employee.first(), many=False)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@renderer_classes([JSONRenderer, XMLRenderer])
@permission_classes([AllowAny])
def create_employee(request: Request) -> Response:
    serializer = EmployeeSerializer(data=request.data)
    if not serializer.is_valid(raise_exception=True):
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer.create(request.data)
    return Response(status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@renderer_classes([JSONRenderer, XMLRenderer])
@permission_classes([AllowAny])
def delete_employee(request: Request, pk: int) -> Response:
    employee = Employee.objects.filter(pk=pk)
    if not employee.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    employee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

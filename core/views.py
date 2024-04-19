from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from .models import *
from .serializers import *


# CLIENT
@api_view(['GET'])
@renderer_classes([JSONRenderer, XMLRenderer])
@permission_classes([AllowAny])
def list_client(request: Request) -> Response:
    clients = Client.objects
    serializer = ClientSerializer(clients, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@renderer_classes([JSONRenderer, XMLRenderer])
@permission_classes([AllowAny])
def detail_client(request: Request, pk: int) -> Response:
    client = Client.objects.filter(pk=pk)
    if not client.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ClientSerializer(client.first(), many=False)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@renderer_classes([JSONRenderer, XMLRenderer])
@permission_classes([AllowAny])
def create_client(request: Request) -> Response:
    serializer = ClientSerializer(data=request.data)
    if not serializer.is_valid(raise_exception=True):
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer.create(serializer.data)
    return Response(status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@renderer_classes([JSONRenderer, XMLRenderer])
@permission_classes([AllowAny])
def delete_client(request: Request, pk: int) -> Response:
    client = Client.objects.filter(pk=pk)
    if not client.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    client.delete()
    return Response(status=status.HTTP_200_OK)


# EMPLOYEE
@api_view(['GET'])
@renderer_classes([JSONRenderer, XMLRenderer])
@permission_classes([AllowAny])
def list_employee(request: Request) -> Response:
    employee = ClientEmployee.objects
    serializer = ClientEmployeeSerializer(employee, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@renderer_classes([JSONRenderer, XMLRenderer])
@permission_classes([AllowAny])
def detail_employee(request: Request, pk: int) -> Response:
    employee = ClientEmployee.objects.filter(pk=pk)
    if not employee.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ClientEmployeeSerializer(employee.first(), many=False)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@renderer_classes([JSONRenderer, XMLRenderer])
@permission_classes([AllowAny])
def create_employee(request: Request) -> Response:
    serializer = ClientEmployeeSerializer(data=request.data)
    if not serializer.is_valid(raise_exception=True):
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer.create(request.data)
    return Response(status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@renderer_classes([JSONRenderer, XMLRenderer])
@permission_classes([AllowAny])
def delete_employee(request: Request, pk: int) -> Response:
    employee = ClientEmployee.objects.filter(pk=pk)
    if not employee.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    employee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

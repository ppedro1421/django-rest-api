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


@api_view(['GET'])
@renderer_classes([JSONRenderer, XMLRenderer])
@permission_classes([AllowAny])
def list_client(request: Request) -> Response:
    clients = Client.objects

    if not clients.exists():
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = ClientSerializer(clients, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@renderer_classes([JSONRenderer, XMLRenderer])
@permission_classes([AllowAny])
def detail_client(request: Request, id: int) -> Response:
    client = Client.objects.filter(id=id)

    if not client.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ClientSerializer(client.first(), many=False)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@renderer_classes([JSONRenderer, XMLRenderer])
@permission_classes([AllowAny])
def create_client(request: Request) -> Response:
    serializer = ClientSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.create(serializer.data)

        return Response(status=status.HTTP_201_CREATED)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@renderer_classes([JSONRenderer, XMLRenderer])
@permission_classes([AllowAny])
def delete_client(request: Request, id: int) -> Response:
    client = Client.objects.filter(id=id)

    if not client.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)

    client.delete()

    return Response(status=status.HTTP_200_OK)

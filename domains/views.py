from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from domains.models import Domain
from domains.serializers import DomainSerializer

# FUNCTIONAL VIEWS


@api_view(['GET', 'POST'])
def domain_list(request, format=None):
    """
    List all domains, or create a new snippet.
    """
    if request.method == 'GET':
        domains = Domain.objects.all()
        serializer = DomainSerializer(domains, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DomainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def domain_detail(request, pk, format=None):
    """
    Retrieve, update or delete a domain.
    """
    try:
        domain = Domain.objects.get(pk=pk)
    except Domain.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DomainSerializer(domain)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DomainSerializer(domain, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        domain.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

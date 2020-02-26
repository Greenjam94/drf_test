from rest_framework import serializers
from servers.models import Server


class ServerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Server
        fields = ['hostname', 'ip', 'created', 'owner']

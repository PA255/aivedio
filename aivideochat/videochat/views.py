from rest_framework import viewsets
from rest_framework.response import Response
from .models import UserConnection
from .serializers import UserConnectionSerializer

class UserConnectionViewSet(viewsets.ModelViewSet):
    queryset = UserConnection.objects.all()
    serializer_class = UserConnectionSerializer

    def create(self, request):
        session_id = request.data.get('session_id')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')
        user_connection, created = UserConnection.objects.get_or_create(
            session_id=session_id,
            defaults={'latitude': latitude, 'longitude': longitude}
        )
        if not created:
            user_connection.latitude = latitude
            user_connection.longitude = longitude
            user_connection.save()
        return Response(UserConnectionSerializer(user_connection).data)
from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api_project_5.permissions import IsOwnerOrReadOnly
from .models import Trip
from .serializers import TripSerializer

class TripList(generics.ListCreateAPIView):
    """
    List all trips
    """
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
        ]
    ordering_fields = [
        'trips_count',
    ]

    def perform_create(self, serializer):
        # Associate the logged-in user as the owner of the trip
        serializer.save(owner=self.request.user)
    
class TripDetail(generics.RetrieveUpdateAPIView):
    serializer_class = TripSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Trip.objects.all()
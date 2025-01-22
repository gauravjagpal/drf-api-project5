from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api_project_5.permissions import IsOwnerOrReadOnly
from .models import Trip
from .serializers import TripSerializer

class TripList(generics.ListAPIView):
    """
    List all trips
    """
    queryset = Trip.objects.annotate(
        trips_count=Count('owner__post', distinct=True),
        ).order_by('-created_at')
    serializer_class = TripSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
        ]
    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
    ]
    ordering_fields = [
        'trips_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]
    
class TripDetail(generics.RetrieveUpdateAPIView):
    serializer_class = TripSerializer
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Trip.objects.annotate(
        trips_count=Count('owner__post', distinct=True)
        ).order_by('-created_at')
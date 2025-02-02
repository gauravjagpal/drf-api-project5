from django.db.models import Count
from rest_framework import generics, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from drf_api_project_5.permissions import IsOwnerOrReadOnly
from .models import Trip
from rest_framework.response import Response
from django_countries import countries
from .serializers import TripSerializer

class TripList(generics.ListCreateAPIView):
    """
    List all trips
    """
    queryset = Trip.objects.all().order_by('-created_at')
    serializer_class = TripSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
        ]
    ordering = ['-id']
    filterset_fields = [
        'owner__profile',
        'country',
        'trip',
        'activities'
    ]
    ordering_fields = [
        'trips_count',
        'country',
        'activities'
    ]

    def perform_create(self, serializer):
        # Associate the logged-in user as the owner of the trip
        serializer.save(owner=self.request.user)
    
class TripDetail(generics.RetrieveUpdateAPIView):
    serializer_class = TripSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Trip.objects.all()

class CountryList(generics.ListAPIView):
    """
    API view to list all countries
    """
    permission_classes = [permissions.AllowAny]
   
    def get_queryset(self):
        # Return the list of all countries as a list of dictionaries
        return [{"name": name} for name in countries]
    
    def list(self, request, *args, **kwargs):
        # Override the `list` method to return the countries as a response
        queryset = self.get_queryset()
        return Response(queryset)
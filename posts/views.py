from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api_project_5.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from django_countries import countries
from .models import Post
from .serializers import PostSerializer



class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Post.objects.annotate(
        favourite_count=Count('favourites', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'favourites__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
        'country'
    ]
    ordering_fields = [
        'favourites_count',
        'comments_count',
        'country'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.annotate(
        comments_count = Count('comment', distinct= True),
        favourites_count = Count('favourites', distinct= True)
    )
    

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
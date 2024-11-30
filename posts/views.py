from django.db.models import Count
from rest_framework import generics, permissions, filters
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
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'favourites_count',
        'comments_count',
        'favourites__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    

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
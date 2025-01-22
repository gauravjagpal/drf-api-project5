from rest_framework import serializers
from .models import Trip
from trips.models import Trip

class TripSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    trip_following_id = serializers.SerializerMethodField()
    trips_count = serializers.ReadOnlyField()
    trip_followers_count = serializers.ReadOnlyField()
    trip_following_count = serializers.ReadOnlyField()
    owner_id = serializers.ReadOnlyField(source='owner.id')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Trip.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Trip
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image', 'is_owner', 'trip_following_id',
            'trips_count', 'trip_followers_count', 'trip_following_count',
            'owner_id'
        ]
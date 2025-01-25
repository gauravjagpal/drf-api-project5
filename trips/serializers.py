from rest_framework import serializers
from .models import Trip

class TripSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    trips_count = serializers.ReadOnlyField()
    owner_id = serializers.ReadOnlyField(source='owner.id')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Trip
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'trip',
            'country', 'image', 'is_owner', 'trips_count',
            'owner_id', 'activities', 'profile_id', 
            'profile_image'
        ]
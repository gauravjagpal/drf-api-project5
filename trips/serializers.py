from rest_framework import serializers
from .models import Trip
from trips.models import Trip

class TripSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    trips_count = serializers.ReadOnlyField()
    owner_id = serializers.ReadOnlyField(source='owner.id')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Trip
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'country', 'image', 'is_owner', 'trips_count',
            'owner_id', 'activities'
        ]
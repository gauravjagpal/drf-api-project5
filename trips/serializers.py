from rest_framework import serializers
from .models import Trip
from django_countries.serializer_fields import CountryField
class TripSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    trips_count = serializers.ReadOnlyField()
    owner_id = serializers.ReadOnlyField(source='owner.id')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    country=CountryField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def validate_country(self, value):
        """
        Validate the country field, defaulting to the current value if not provided.
        """
        # If the value is not set during update, use the existing instance value
        if not value and self.instance:
            return self.instance.country
        print(value)
        return value
    
    def to_representation(self, instance):
        """Modify the representation to add the country_name field."""
        # Get the default representation from the parent class
        representation = super().to_representation(instance)
        # Add the country name to the representation
        representation['country'] = instance.country.name  # Country name instead of code
        return representation

    class Meta:
        model = Trip
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'trip',
            'country', 'image', 'is_owner', 'trips_count',
            'owner_id', 'activities', 'profile_id', 
            'profile_image'
        ]
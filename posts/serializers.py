from rest_framework import serializers
from posts.models import Post
from favourites.models import Favourite


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    favourite_id = serializers.SerializerMethodField()
    favourites_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()


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
    
    
    def get_favourite_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            favourite = Favourite.objects.filter(
                owner=user, post=obj
            ).first()
            return favourite.id if favourite else None
        return None
    
    def validate_country(self, value):
        """
        Validate the country field, defaulting to the current value if not provided.
        """
        # If the value is not set during update, use the existing instance value
        if not value and self.instance:
            return self.instance.country
        return value
    
    def to_representation(self, instance):
        """Modify the representation to add the country_name field."""
        # Get the default representation from the parent class
        representation = super().to_representation(instance)
        # Add the country name to the representation
        representation['country'] = instance.country.name  # Country name instead of code
        return representation


    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'country',
            'favourite_id', 'favourites_count', 'comments_count',
        ]
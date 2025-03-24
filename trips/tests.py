from django.contrib.auth.models import User
from .models import Trip
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import io
class TripViewTests(APITestCase):
    def setUp(self):
        self.alex = User.objects.create_user(username='Alex', password='pass')
        self.bob = User.objects.create_user(username='Bob', password='pass')
        self.alex_trip = Trip.objects.create(owner=self.alex, trip="Alex's trip", country="IN")
        self.bob_trip = Trip.objects.create(owner=self.bob, trip="Bob's trip", country="US")
    
    def test_can_list_trip(self):
        Alex = User.objects.get(username='Alex')
        Trip.objects.create(owner=Alex, trip='a trip')
        self.client.login(username='Alex', password='pass')
        response = self.client.get('/trips/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))
    
    def generate_test_image(self):
        """Create an actual image file for testing"""
        image_io = io.BytesIO()
        image = Image.new("RGB", (100, 100), "blue")  # 100x100px blue image
        image.save(image_io, format="JPEG")
        image_io.seek(0)
        return SimpleUploadedFile("test.jpg", image_io.read(), content_type="image/jpeg")
    
    def test_logged_in_user_can_create_trip(self):
        Trip.objects.all().delete()
        self.client.login(username='Alex', password='pass')
        image = self.generate_test_image()
        response = self.client.post('/trips/', {
            'trip': 'a trip',
            'country': 'IN',
            'image': image
            })
        count = Trip.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_user_not_logged_in_cant_create_trip(self):
        Trip.objects.all().delete()
        image = self.generate_test_image()
        response = self.client.post('/trips/', {
            'trip': 'a trip',
            'country': 'IN',
            'image': image
            })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_logged_in_user_can_delete_own_trip(self):
        self.client.login(username='Alex', password='pass')
        initial_count = Trip.objects.count()
        # Send the DELETE request to delete Alex's trip
        response = self.client.delete(f'/trips/{self.alex_trip.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Check that Alex's trip is deleted, and only Bob's trip remains
        self.assertEqual(Trip.objects.count(), initial_count - 1)


    def test_user_cannot_delete_others_trip(self):
        Trip.objects.all().delete()
        another_user = User.objects.create_user(username='Bobby', password='pass')
        another_trip = Trip.objects.create(owner=another_user, trip='Bobby\'s trip', country='US')
        self.client.login(username='Alex', password='pass')
        response = self.client.delete(f'/trips/{another_trip.id}/')
        # Check that the status code is 403 (Forbidden), since Alex should not be able to delete Bob's trip
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Verify that the trip still exists
        self.assertEqual(Trip.objects.count(), 2)  # Both trips should still exist
from django.contrib.auth.models import User
from .models import Trip
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import io
class TripViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='Alex', password='pass')
    
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
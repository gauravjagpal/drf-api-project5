from django.contrib.auth.models import User
from .models import Trips
from rest_framework import status
from rest_framework.test import APITestCase

class ListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='Alex', password='pass')
    
    def test_can_list_trip(self):
        Alex = User.objects.get(username='Alex')
        Trips.objects.create(owner=Alex, title='a title')
        response = self.client.get('/trips/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))
    
    def test_logged_in_user_can_create_trip(self):
        self.client.login(username='Alex', password='pass')
        response = self.client.post('/trips/', {'title': 'a title'})
        count = Trips.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_user_not_logged_in_cant_create_trip(self):
        response = self.client.post('/trips/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import io
class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='Alex', password='pass')

    def test_can_list_posts(self):
        Alex = User.objects.get(username='Alex')
        Post.objects.create(owner=Alex, title='a title')
        response = self.client.get('/posts/')
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
    

    def test_logged_in_user_can_create_post(self):
        self.client = APIClient()
        user = User.objects.get(username='Alex')
        self.client.force_authenticate(user=user)
        image = self.generate_test_image()  # Use real image
        response = self.client.post(
            '/posts/',
            {
                'title': 'a title',
                'content': 'Test content',
                'image': image,
                'country': 'IN'
            },
            format='multipart'
        )
        print("Response Status Code:", response.status_code)
        print("Response Data:", response.data)
        print("Post Count:", Post.objects.count())

        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        response = self.client.post('/posts/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        Alex = User.objects.create_user(username='Alex', password='pass')
        George = User.objects.create_user(username='George', password='pass')
        Post.objects.create(
            owner=Alex, title='a title', content='Alexs content'
        )
        Post.objects.create(
            owner=George, title='another title', content='Georges content'
        )

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        response = self.client.get('/posts/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def generate_test_image(self):
        """Create an actual image file for testing"""
        image_io = io.BytesIO()
        image = Image.new("RGB", (100, 100), "blue")  # 100x100px blue image
        image.save(image_io, format="JPEG")
        image_io.seek(0)
        return SimpleUploadedFile("test.jpg", image_io.read(), content_type="image/jpeg")
    
    def test_user_can_update_own_post(self):
        self.client.login(username='Alex', password='pass')
        image = self.generate_test_image()
        response = self.client.put(
            '/posts/1/',
            {
                'title': 'a new title',
                'content': 'Test content',
                'image': image,
                'country': 'IN'
            },
            format='multipart'
        )
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        self.client.login(username='Alex', password='pass')
        response = self.client.put('/posts/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

import unittest

from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.test import Client
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
# Create your tests here.
from rest_framework.test import APITestCase

from .models import UserProfile, User, Comment, Ad


# class TestUserOperations(APITestCase):
class TestUserOperations(TestCase):
    def test_register_user(self):
        url = reverse('register')
        data = {
            "username": "testuser",
            "email": "existing_user@example.com",
            "password1": "password@123",
            "password2": "password@123",
        }
        response = self.client.post(url, data, format='json')
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response)
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], 'testuser')
        self.assertEqual(response.data['email'], 'testuser@example.com')

# class TestRegistration(TestCase):
#     def setUp(self):
#         self.client = Client()

#     def test_registration_success(self):
#         url = reverse('register')
#         data = {
#             'username': 'testuser',
#             'email': 'testuser@example.com',
#             'password1': 'password@123',
#             'password2': 'password@123',

#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, 302)
#         self.assertIn('/ads/login/', response['Location'])
#         self.assertEqual(UserProfile.objects.count(), 1)
#         self.assertEqual(User.objects.count(), 1)

#     # def test_registration_failure_invalid_username(self):
#     #     data = {
#     #         'username': 'invalid-username',
#     #         'email': 'testuser@example.com',
#     #         'password1': 'password',
#     #         'password2': 'password'
#     #     }
#     #     url = reverse('register')
#     #     response = self.client.post(url, data, format='json')
#     #     self.assertEqual(response.status_code, 200)
#     #     self.assertIn('Invalid username', response.content.decode())

#     def test_registration_failure_duplicate_email(self):
#         # Create a user with the same email address
#         User.objects.create_user(
#             'existing_user', 'existing_user@example.com', 'password')
#         data = {
#             "username": "testuser",
#             "email": "existing_user@example.com",
#             "password1": "password@123",
#             "password2": "password@123',
#         }
#         url = reverse('register')
#         # response = self.client.post(url, data, format='json')
#         # # response = self.client.post('/registration/register/', data)
#         # self.assertEqual(response.status_code, 200)
#         # self.assertIn('Email address already in use',
#         #               response.content.decode())
#         with self.assertRaises(IntegrityError):
#             self.client.post(url, data, format='json')

#     def test_login(self):

#         User.objects.create(
#             username='testuser',
#             email='existing_user@example.com',
#             password='password@123',

#         )
#         data1 = {
#             'username': 'testuser',
#             'password': 'password@123',
#         }
#         data2 = {
#             'username': 'user1',
#             'password': 'user1@password',
#         }
#         url = reverse('login')
#         response = self.client.post(url, data1, format='json', follow=True)
#         print(User.objects.all())
#         self.assertEqual(User.objects.count(), 1)
#         print('login response', response)
#         print('user:', response.context['user'])
#         # # print("session:", response.context)
#         # for key in response.context.keys():
#         #     print("key", key, ":", response.context[key])
#         # self.assertTrue(self.client.session['_auth_user_id'])
#         self.assertTrue(response.context['user'].is_authenticated)
#         # self.assertEqual(response.status_code,)

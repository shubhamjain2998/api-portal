from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_jwt.settings import api_settings

from portal.models import Book, Category

payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()


class PortalAPITestCase(APITestCase):
    def setUp(self):
        user_obj = User(username='testadmin', email='test@test.com')
        user_obj.set_password("admin123")
        user_obj.save()
        Category.objects.create(name='test')
        cat = Category.objects.first()
        Book.objects.create(book_name='abcd', book_course_name='efgh', category=cat)

    def test_get_books_with_user(self):
        book = Book.objects.first()
        data = {}
        url = book.get_api_url()

        user_obj = User.objects.first()
        payload = payload_handler(user_obj)
        token_rsp = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_rsp)

        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)

from django.test import TestCase
from .models import Logo, Tag, LogoTag, Category
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

# Create your tests here.


class Test(APITestCase):

    def test_create(self):
        url = reverse('logos')
        data = {"name": "logo", "category": "category_name",
                "formats": [
                        {"extension": "png", "image_url": "url"},
                        {"extension": "jpg", "image_url": "url2"}
                ],
                "tags": [
                    {"name": "tag"},
                    {"name": "tag2"}
                ]}
        response = self.client.post(url, data, format='json')

        logo = Logo.objects.get(name='logo')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(logo.category.name, 'category_name')
        self.assertEqual(Tag.objects.filter(logo=logo).count(), 2)
        self.assertEqual(LogoTag.objects.filter(logo=logo).count(), 2)

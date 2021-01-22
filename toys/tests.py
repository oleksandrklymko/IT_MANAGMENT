from django.test import TestCase, Client
from django.urls import reverse

from .models import Toy


class MyTestCase(TestCase):
    def setUp(self):
        self.toy = Toy.objects.create(title='Lego', price=200, description='For kids 3+', picture='../media/images/gam1.jpeg')

    def test_toys_list(self):
        client = Client()
        response = client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'toys/toys.html')

    def test_get_existing_toy(self):
        self.assertEqual(self.toy.pk, 1)

    def test_get_toy_that_dont_exist(self):
        self.assertEqual(self.toy.pk, 2)

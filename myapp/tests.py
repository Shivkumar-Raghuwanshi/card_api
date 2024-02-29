from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Card, Delivered, DeliveryException, Pickup, Returned
from django.utils import timezone

class GetCardStatusTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.card = Card.objects.create(card_id='test_card', user_contact='test_contact')
        Delivered.objects.create(id='test_delivered', card=self.card, timestamp=timezone.now(), comment='test_comment')
        DeliveryException.objects.create(id='test_delivery_exception', card=self.card, timestamp=timezone.now(), comment='test_comment')
        Pickup.objects.create(id='test_pickup', card=self.card, timestamp=timezone.now())
        Returned.objects.create(id='test_returned', card=self.card, timestamp=timezone.now())

    def test_get_card_status_by_card_id(self):
        response = self.client.get(reverse('get_card_status'), {'query': 'test_card'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Delivered', response.data)
        self.assertIn('DeliveryException', response.data)
        self.assertIn('Pickup', response.data)
        self.assertIn('Returned', response.data)

    def test_get_card_status_by_user_contact(self):
        response = self.client.get(reverse('get_card_status'), {'query': 'test_contact'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Delivered', response.data)
        self.assertIn('DeliveryException', response.data)
        self.assertIn('Pickup', response.data)
        self.assertIn('Returned', response.data)

    def test_get_card_status_no_query(self):
        response = self.client.get(reverse('get_card_status'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_card_status_card_not_found(self):
        response = self.client.get(reverse('get_card_status'), {'query': 'nonexistent_card'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

from django.test import TestCase
from .models import Station

class StationsTests(TestCase):
    def test_create_station(self):
        s = Station.objects.create(name='Main', code='ST001')
        self.assertEqual(str(s), 'ST001 - Main')

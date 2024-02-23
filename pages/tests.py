from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from pages.views import home_view
from django.http import HttpResponse


class SampleTestCase(TestCase):
    def testsample(self):
        res = home_view("test")
        self.assertEqual(HttpResponse.status_code, res.status_code)

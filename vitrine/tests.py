from django.test import TestCase

# Create your tests here.
class TestCase(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

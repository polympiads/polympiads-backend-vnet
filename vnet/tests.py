from django.test import TestCase

from polympiads.contrib.auth.models import User

class TestHelloWorld (TestCase):
    def test_setup (self):
        user = User.objects.create_user("hello")
        self.assertEqual(user.username, "hello")

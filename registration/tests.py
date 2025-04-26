from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        # Create a user instance
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_profile_create(self):
        exists = Profile.objects.filter(user__username='testuser').exists()
        self.assertTrue(exists, True)
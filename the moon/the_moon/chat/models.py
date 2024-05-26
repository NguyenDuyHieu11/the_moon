from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    # Add your custom user fields here
    phone_number = models.CharField(max_length=20, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)

    REQUIRED_FIELDS = ['email', 'phone_number']  # Add required fields here

    def __str__(self):
        return self.username
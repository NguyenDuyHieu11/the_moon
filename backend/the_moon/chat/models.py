from django.db import models
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint
import datetime
# class CustomUser(User):
#     # Add your custom user fields here
#     phone_number = models.CharField(max_length=20, blank=True)
#     bio = models.TextField(max_length=500, blank=True)
#     profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)

#     REQUIRED_FIELDS = ['email', 'phone_number']  # Add required fields here

#     def __str__(self):
#         return self.username
def get_default_user_profile():
    return UserProfile.objects.get_or_create(
        phone_number='default_number', 
        email='default_email@example.com'
    )[0]
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length = 15, null = False)
    email = models.CharField(max_length = 255, null = False)
    name = models.CharField(max_length = 255)
    age = models.IntegerField()
    location = models.CharField(max_length = 255)

    class Meta():
        constraints = [
            UniqueConstraint(fields=["phone_number", "email"], name="UserProfilePK")
        ]
        
class UserJob(models.Model):
    job = models.CharField(max_length = 255)
    user_profile = models.ForeignKey(UserProfile, default = get_default_user_profile, on_delete = models.CASCADE)

class School(models.Model):
    school_title = models.CharField(max_length = 255)
    start_time = models.DateField()
    end_time = models.DateField()
    activity = models.CharField(max_length = 255)
    user_profile = models.ForeignKey(UserProfile, default = get_default_user_profile, on_delete = models.CASCADE)

    class Meta():
        constraints = [
            UniqueConstraint(fields=["school_title", "start_time"], name="SchoolPK")
        ]

class OneOnOneChat(models.Model):
    receiver_email = models.CharField(max_length = 255)
    receiver_phone_number = models.CharField(max_length=15)
    message = models.JSONField() 
    user_profile = models.ForeignKey(UserProfile, default = get_default_user_profile, on_delete = models.CASCADE) 
    
class NoteOnFeed(models.Model):
    note = models.CharField(max_length = 60)
    user_profile = models.ForeignKey(UserProfile, default = get_default_user_profile, on_delete = models.CASCADE)


class ImageOnFeed(models.Model):
    user_profile = models.ForeignKey(UserProfile, default = get_default_user_profile, on_delete = models.CASCADE)
    uploaded_at = models.DateField(default = datetime.date.today, null = False)
    image = models.BinaryField(default=b'\x08', null = False)


    
    
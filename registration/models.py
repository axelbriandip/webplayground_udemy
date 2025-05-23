from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

def custom_profile_picture_path(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.profile_picture.delete()
    return 'profile_pictures/' + filename

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to=custom_profile_picture_path, blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['user__username']

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        # print("Profile created for user:", instance.username)
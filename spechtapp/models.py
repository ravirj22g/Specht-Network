from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(default="Specht (Default)", max_length=50)
    location = models.CharField(max_length=50)
    bio = models.TextField()
    profile_img = models.ImageField(default='images/default.jpg',
                                    upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.name

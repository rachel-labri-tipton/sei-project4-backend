from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, User
# Create your models here.


class CommunityUser(AbstractUser):
    profile_image = models.ImageField(null=True)
    # community_groups=models.ManyToManyField()
    bio = models.TextField(null=True, default=False)
    is_author = models.BooleanField(default=False)
    is_communityleader = models.BooleanField(default=False)

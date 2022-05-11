from django.db import models
from blog_posts.models import BlogPost
from users.models import CommunityUser

# Create your models here.


class Comment(models.Model):

    body = models.TextField(blank=False)
    user = models.ForeignKey(
        CommunityUser, related_name='comments', on_delete=models.CASCADE)
    blogpost = models.ForeignKey(
        BlogPost, related_name='comments', on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

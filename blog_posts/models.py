from django.db import models
from blog_categories.models import Category
from users.models import CommunityUser
import media

# Create your models here.


class BlogPost(models.Model):

    OPTIONS = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    # categories = models.ManyToManyField(
    #     Category, blank=True,  related_name="blog_posts")

    image = models.TextField(max_length=200)

    title = models.CharField(max_length=200, unique=True)

    excerpt = models.TextField(null=True)

    # author = models.ForeignKey(
    #     users.CommunityUser, on_delete=models.CASCADE, related_name='blogposts', null=True)

    author = models.ForeignKey(
        "users.CommunityUser", on_delete=models.CASCADE, related_name='blogposts', null=True, blank=True)

    content = models.TextField()

    categories = models.ManyToManyField(
        Category, related_name='article_categories', blank=True)

    status = models.CharField(
        max_length=10, choices=OPTIONS, default='draft')

    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

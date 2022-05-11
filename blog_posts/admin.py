from django.contrib import admin

from blog_posts.models import BlogPost
from django_summernote.admin import SummernoteModelAdmin


class BlogPostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content', 'excerpt')


# Register your models here.
admin.site.register(BlogPost, BlogPostAdmin)

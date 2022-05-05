from django.urls import path

from blog_posts.views import BlogPostListView, BlogPostDetailView

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogpostlist'),
    path('<int:pk>/', BlogPostDetailView.as_view(), name='oneblogpost')
]

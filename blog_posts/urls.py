from django.urls import path

from blog_posts.views import BlogPostListDetailfilter, BlogPostListView, BlogPostDetailView, BlogPostStaffWriterView

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogpostlist'),
    path('<int:pk>/', BlogPostDetailView.as_view(), name='oneblogpost'),
    path('authorpage/', BlogPostStaffWriterView.as_view()),
    path('search/', BlogPostListDetailfilter.as_view())
]

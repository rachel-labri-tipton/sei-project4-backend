
from django.urls import path
from blog_comments.views import CommentDetail, CommentList


urlpatterns = [
    path('', CommentList.as_view()),
    path('<int:pk>', CommentDetail.as_view())
]

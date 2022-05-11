from django.urls import path
from users.views import ProfileUpdateDetailView, RegisterView, ProfileView, ProfileDetailView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('', ProfileView.as_view()),
    path('profile/<int:pk>/', ProfileDetailView.as_view()),
    path('profile/update/<int:pk>/', ProfileUpdateDetailView.as_view())
]

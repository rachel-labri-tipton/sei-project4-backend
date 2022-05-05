from django.urls import path
from users.views import IsAuthorView, RegisterView, LoginView, ProfileView, ProfileDetailView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('isauthor/', IsAuthorView.as_view()),
    path('', ProfileView.as_view()),
    path('profile/<int:pk>/', ProfileDetailView.as_view())
]

from django.urls import path

from users.views import LoginView, UserIdDeleteView, UserIdView, UserView

urlpatterns = [
    path('users/', UserView.as_view()),
    path('users/<str:id>/', UserIdView.as_view()),    
    path('users/delete/<str:id>/', UserIdDeleteView.as_view()),    
    path('users/register/', LoginView.as_view()),    
]

from django.urls import path

from users.views import LoginView, UserIdDeleteView, UserIdView, UserView

urlpatterns = [
    path('users/', UserView.as_view()),
    path('users/<int:user_id>/', UserIdView.as_view()),    
    path('users/<int:user_id>/', UserIdDeleteView.as_view()),    
    path('users/register/', LoginView.as_view()),    
]

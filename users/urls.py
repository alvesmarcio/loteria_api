from django.urls import path

from users.views import LoginView, UserIdView, UserNumberView, UserView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<str:id>/", UserIdView.as_view()),
    path("users/<str:id>/number/", UserNumberView.as_view()),
    path("login/", LoginView.as_view()),
]

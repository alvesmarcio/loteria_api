from django.urls import path

from user_numbers.views import UserNumberCreateView, UserNumberIdView


urlpatterns = [
    path("numbers/", UserNumberCreateView.as_view()),
    path("numbers/<str:id>/", UserNumberIdView.as_view()),
]

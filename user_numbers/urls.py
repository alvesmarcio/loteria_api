from django.urls import path

from user_numbers.views import UserNumberIdView, UserNumberView


urlpatterns = [
    path("numbers/", UserNumberView.as_view()),
    path("numbers/<int:id>/", UserNumberIdView.as_view()),
]

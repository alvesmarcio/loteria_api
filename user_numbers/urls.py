from django.urls import path

from user_numbers.views import UserNumberView


urlpatterns = [
    path("numbers/", UserNumberView.as_view()),
]

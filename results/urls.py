from django.urls import path

from results.views import ListCreateView, RetrieveUpdateDestroyView


urlpatterns = [
    path("results/", ListCreateView.as_view()),
    path("results/<int:concurso>/", RetrieveUpdateDestroyView.as_view()),
]

from django.urls import path

from results.views import RetrieveUpdateDestroyView, GetListResultsView, CreateView


urlpatterns = [
    path("results/new_contest/", CreateView.as_view()),
    path("results/", GetListResultsView.as_view()),
    path("results/<int:concurso>/", RetrieveUpdateDestroyView.as_view()),
]

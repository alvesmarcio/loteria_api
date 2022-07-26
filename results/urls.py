from django.urls import path

from results.views import RetrieveUpdateDestroyView, GetListResultsView, CreateView


urlpatterns = [
    path("results/", CreateView.as_view()),
    path("results/<int:concurso>/", RetrieveUpdateDestroyView.as_view()),
    path("results/admin/", GetListResultsView.as_view()),
]

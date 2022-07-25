from django.urls import path

from results.views import CreateUpdateDestroyView, ListRetrieveView


urlpatterns = [
    path('results/', ListRetrieveView.as_view()),
    path("results/<int:concurso>/", CreateUpdateDestroyView.as_view())
]

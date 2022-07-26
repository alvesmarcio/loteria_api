"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions


# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# schema_view = get_schema_view(
#     openapi.Info(
#       title="LOTERIA API",
#       default_version='v1',
#       description="API destinada a geração de numeros para megasena baseados em algoritimos matematicos",
#     #   terms_of_service="",
#     #   contact=openapi.Contact(email="contact@snippets.local"),
#     #   license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=[permissions.AllowAny],
# )

from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

schema_view = get_schema_view(
    title="LotoApi",
    description="Sorteador de numeros inteligente para jogar loteria!"
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("users.urls")),
    path("LotoAPI", schema_view, name="LotoAPI"),
    path("", TemplateView.as_view(
        template_name="swagger-ui.html",
        extra_context={'schema_url':'LotoAPI'}
    ), name='swagger-ui'),
    path("api/", include("user_numbers.urls")),
    path("api/", include("results.urls")),
]
# urlpatterns += [
#    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#    path('', TemplateView.as_view(template_name='swagger-ui.html',
#         extra_context={'schema_url':'openapi-schema'}
#     ), name='swagger-ui')
# ]
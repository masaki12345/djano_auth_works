from django.urls import path
from django.contrib import admin
from django.conf.urls import include, url

# swagger導入URL
from rest_framework import permissions, authentication
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# from .views import PostList, PostDetail

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
    authentication_classes=(authentication.SessionAuthentication,),
)

urlpatterns = [
  
]

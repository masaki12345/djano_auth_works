from django.urls import path
from django.contrib import admin
from django.conf.urls import include, url

# swagger導入URL
from rest_framework import permissions, authentication
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_auth.views import (
    LoginView, LogoutView, UserDetailsView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView
)


urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'),),  # 追加
    path('account/', include('allauth.urls')),
    path('^password/change/$', PasswordChangeView.as_view(),
         name='rest_password_change',),
]

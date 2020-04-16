from django.urls import path
from django.contrib import admin
from django.conf.urls import include, url
from rest_framework import routers, permissions, authentication
# swagger導入URL


# from rest_auth.views import (
#     LoginView, LogoutView, UserDetailsView, PasswordChangeView,
#     PasswordResetView, PasswordResetConfirmView
# )

# app_name = 'rest_framework'
urlpatterns = [
    path('', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'),),  # 追加
    url(r'^account/', include('allauth.urls')),



]

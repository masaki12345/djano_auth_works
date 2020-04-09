from django.urls import path
from django.contrib import admin
from django.conf.urls import include, url

from rest_framework import permissions, authentication
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='API Lists')

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Snippets API",
#         default_version='v1',
#         description="Test description",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="contact@snippets.local"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.IsAuthenticated,),
#     authentication_classes=(authentication.SessionAuthentication,),
# )
app_name = 'rest_framework'
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'rest-auth/', include('rest_auth.urls')),

    path('api/v1/rest-auth/', include('rest_auth.urls')),  # 追加
    path('api/v1/rest-auth/registration/',
         include('rest_auth.registration.urls')),  # 追加
    path('account/', include('allauth.urls')),
    # path('docs/', include('rest_auths.urls')),
    url(r'^swagger/', schema_view),
]

from django.urls import path, include


urlpatterns = [
    path('rest-api/', include('rest_framework.urls')),
]
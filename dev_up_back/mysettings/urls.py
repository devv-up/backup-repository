from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-api/', include('rest_framework.urls')),
    path('', include('dev_up_api.urls'))
]

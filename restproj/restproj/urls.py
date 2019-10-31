from django.contrib import admin
from django.urls import path, include
from mystorage import urls
from rest_framework import urls
from djago.conf import settings
from django.con.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mystorage.urls')),
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
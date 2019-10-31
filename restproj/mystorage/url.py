from rest_framework.routers import DefaultRouter
from django.urls import path, include
from mystroage import views


router = DefaultRouter()
router.register('essay', views.PostViewSet)
router.register('album', views.ImgviewSet)
router.register('files', views.FileViewSet)

urlpatterns = [
    path('',include(router.urls)),
    #path('',include('mystorage.urls')),
    #path('api-auth/', include('rest_framework.urls'))
]
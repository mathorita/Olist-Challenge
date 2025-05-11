from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from Olist.views import AuthorViewSet,BookViewSet

router = routers.DefaultRouter()
router.register('author', AuthorViewSet, basename='Author')
router.register('book',BookViewSet,basename='Book')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]

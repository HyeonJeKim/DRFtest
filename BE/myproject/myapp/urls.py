from django.urls import path, include
from . import views
from .views import HelloAPI

urlpatterns = [
    path("", views.index, name='index'),
    path("hello/", HelloAPI),
]
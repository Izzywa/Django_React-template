from django.urls import path

from . import views

app_name = 'backend' # insert app name

urlpatterns = [
    path('', views.index, name='index'),
]
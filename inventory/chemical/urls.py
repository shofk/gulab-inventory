from django.urls import path

from . import views

app_name = 'chemical'
urlpatterns = [
    path('', views.index, name='index')
]

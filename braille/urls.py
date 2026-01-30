from django.urls import path
from . import views

app_name = 'braille'
urlpatterns = [
    path('', views.index, name='index')
]
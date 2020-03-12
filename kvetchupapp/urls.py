from django.urls import path
from . import views

app_name = 'kvetchupapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('getSite/', views.getSite, name='getSite')
]
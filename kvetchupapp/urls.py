from django.urls import path
from . import views

app_name = 'kvetchupapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('getSite/', views.getSite, name='getSite'),
    path('login/', views.login, name='login'),
    path('sendmail/', views.send, name='sendmail'),
    path('ratings/', views.ratings, name="ratings")
]
from django.urls import path
from . import views

app_name = 'kvetchupapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('getSite/', views.getSite, name='getSite'),
    path('login/', views.login, name='login'),
    path('sendmail/', views.send, name='sendmail'),
    path('reviews/', views.ratings, name="ratings"),
    path('newreview/', views.new_review, name="newreview"),
    path('profile/', views.profile, name="profile")
]
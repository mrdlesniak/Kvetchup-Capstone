from django.urls import path
from . import views

app_name = 'kvetchupapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('reviews/', views.ratings, name="ratings"),
    path('profile/', views.profile, name="profile"),
    path('about/', views.about, name='about'),
    path('getSite/', views.getSite, name='getSite'),
    path('login/', views.login, name='login'),
    path('sendmail/', views.send, name='sendmail'),
    path('newreview/', views.new_review, name="newreview"),
    path('edit/', views.edit, name="edit"),
    path('editReview/', views.edit_review, name="edit_review"),
    path('deleteReview/', views.delete_review, name="delete_review")
]
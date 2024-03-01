from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('',views.index ,name="home"),
    path('about/',views.about,name="about"),
    path('posts/',views.posts,name="posts"),
    path('add',views.add,name="add"),
    path('blog/<id>',views.detailed,name="detailed"),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/',views.edit,name='edit'),
 ]
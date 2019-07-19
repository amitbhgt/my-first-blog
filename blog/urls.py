from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('about_us', views.about_us, name='about_us'),
    path('post_page', views.single_post, name='single_post'),
]
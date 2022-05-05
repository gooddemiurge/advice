from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.Main_page.as_view(), name='index'),
    path('about_us', views.about_us, name='about'),
    path('add_post', views.add_post, name='add_post'),
    url('register', views.register, name='register'),
    path('login', views.login, name='login')
]
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.MainPage.as_view(), name='index'),
    path('<int:pk>', views.PostDetail.as_view(), name='detail'),
    path('add_post', views.add_post, name='add_post'),
    url('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('posts', views.MyPosts.as_view(), name='posts'),
    path('delete/<int:pk>', views.delete_post, name='delete'),
    path('del_ans/<int:pk>', views.delete_answer, name='del_ans'),
    path('status/<int:pk>', views.change_status, name='status'),
    path('edit/<int:pk>', views.EditPost.as_view(), name='edit'),
    path('logout', views.logout, name='logout'),
    path('search', views.Search.as_view(), name='search')
]
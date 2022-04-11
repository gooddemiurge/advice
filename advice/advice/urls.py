from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from advice.advice_app import views

urlpatterns = [
    path('about_us/', include('advice_app.urls')),
    path('admin/', admin.site.urls),
    path('', include('advice_app.urls')),
    url(r'^register/$', views.register, name='register')
]

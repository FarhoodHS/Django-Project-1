from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='home'),
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('count/', views.count, name='count'),

]

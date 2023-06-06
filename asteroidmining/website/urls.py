from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import MyLoginView


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', MyLoginView.as_view(), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('upload/', views.upload_image, name='upload_image'),
    path('user_authentication/', views.user_authentication, name='user_authentication'),
]

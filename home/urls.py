from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('gallery', views.gallery, name='gallery'),
    path('login', views.login_view, name='login'),
    path('pricing', views.price, name='pricing'),
    path('signup', views.handleSignup, name='signup'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('logout', views.logout_view, name='logout')
]
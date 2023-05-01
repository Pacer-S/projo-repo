from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/profile/', views.profile, name="profile"),
    path('add_product', views.add_product, name='add_product'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('accesories', views.accesories, name='accesories'),
    path('about', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('signup/', views.signup, name = 'signup'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
]

from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Jeet Cycle Stores Admin"
admin.site.site_title = "Jeet Cycle Stores Admin Portal"
admin.site.index_title = "Welcome to Jeet Cycle Stores"


urlpatterns = [
    path('', views.index, name = 'home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('bicycles', views.bicycles, name='bicycles'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('cart', views.cart, name='cart'),
    
    
]

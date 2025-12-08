from django.contrib import admin
from django.urls import path

from web import views

app_name='web'

urlpatterns = [
    path('', views.index, name='index'), 
    path('about/', views.about, name= 'about') , 
    path('product/<int:id>/', views.product, name= 'product') ,
    path('contact/', views.contact, name= 'contact') , 
    path('product_gallery/<int:id>/', views.product_gallery, name= 'product_gallery'),
    path('gallery/', views.gallery, name= 'gallery'),
    path('gallery-images/<int:category_id>/', views.gallery_images, name='gallery_images'),
    path('visualise/', views.visualise, name= 'visualise'),
    
]

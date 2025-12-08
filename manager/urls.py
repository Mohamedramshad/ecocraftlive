from django.urls import path
from manager import views

app_name = 'manager'


urlpatterns = [
    path('logout/', views.manager_logout, name='logout'),
    path('login/', views.manager_login, name='login'),
    path('slider/', views.slider, name='slider'),
    path('slider_add/', views.slider_add, name='slider_add'),
    path('slider_edit/<int:id>/', views.slider_edit, name='slider_edit'),
    path('slider_delete/<int:id>/', views.slider_delete, name='slider_delete'),
    path('legacy/', views.legacy, name='legacy'),
    path('legacy_add/', views.legacy_add, name='legacy_add'),
    path('legacy_edit/<int:id>/', views.legacy_edit, name='legacy_edit'),
    path('legacy_delete/<int:id>/', views.legacy_delete, name='legacy_delete'),
    path('aboutbox/', views.aboutbox, name='aboutbox'),
    path('aboutbox_add/', views.aboutbox_add, name='aboutbox_add'),
    path('aboutbox_edit/<int:id>/', views.aboutbox_edit, name='aboutbox_edit'),
    path('aboutbox_delete/<int:id>/', views.aboutbox_delete, name='aboutbox_delete'),
    path('product_category/', views.product_category, name='product_category'),
    path('product_category_add/', views.product_category_add, name='product_category_add'),
    path('product_category_edit/<int:id>/', views.product_category_edit, name='product_category_edit'),
    path('product_category_delete/<int:id>/', views.product_category_delete, name='product_category_delete'),
    path('product_feature/', views.product_feature, name='product_feature'),
    path('product_feature_add/', views.product_feature_add, name='product_feature_add'),
    path('product_feature_edit/<int:id>/', views.product_feature_edit, name='product_feature_edit'),
    path('product_feature_delete/<int:id>/', views.product_feature_delete, name='product_feature_delete'),
    path('', views.product, name='product'),
    path('product_add/', views.product_add, name='product_add'),
    path('product_edit/<int:id>/', views.product_edit, name='product_edit'),
    path('product_delete/<int:id>/', views.product_delete, name='product_delete'),
    path('gallery_category/', views.gallery_category, name='gallery_category'),
    path('gallery_category_add/', views.gallery_category_add, name='gallery_category_add'),
    path('gallery_category_edit/<int:id>/', views.gallery_category_edit, name='gallery_category_edit'),
    path('gallery_category_delete/<int:id>/', views.gallery_category_delete, name='gallery_category_delete'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery_add/', views.gallery_add, name='gallery_add'),
    path('gallery_edit/<int:id>/', views.gallery_edit, name='gallery_edit'),
    path('gallery_delete/<int:id>/', views.gallery_delete, name='gallery_delete'),
]
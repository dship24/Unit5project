"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from app import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name="home"),
    path('admin-page/', views.admin_page, name="admin"),
    path('user-page/', views.user, name="user"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('update_product/<str:name>/', views.update_product, name="update product"),
    path('create_product/', views.create_product, name="create product"),
    path('delete/<str:id>/', views.delete_order, name="delete"),
    path('user_orders/<str:name>/', views.user_orders, name="user orders"),
    path('delete_product/<str:name>/', views.delete_product, name="delete product"),
    path('update_order/<str:id>/<str:status>/', views.update_order, name="update order"),
    path('order_product/<str:name>/', views.order_item, name="order item")
]

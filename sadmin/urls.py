"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from.import views

urlpatterns = [
    path('home/', views.admin_home, name='home'),
    path('', views.getlogin, name="login"),
    path('logout/', views.getlogout, name="logout"),


    path('user_register/', views.add_users, name='user_register'),
    path('user_list/<str:filter>/', views.user_list, name="user_list"),
    path('user_view/<int:id>/', views.view_user, name="user_view"),
    path('user_update/<str:username>/', views.update_user, name="user_update"),
    path('user_view/<int:id>/', views.view_user, name="user_view"),
    path('delete_user/<int:id>/', views.user_delete, name="delete_user"),

    path('blog_list/', views.all_blog, name='blog_list'),
    path('add_new_blog/', views.add_new_blog, name='add_new_blog'),
    path('view_blog/<int:id>/', views.view_blog, name='blog_view'),
    path('update_blog/<int:id>/', views.update_blog, name='update_blog'),
    path('delete_blog/<int:id>/', views.delete_blog, name='delete_blog'),

    path('contact_list/', views.contacts_list, name='contact_list'),
    path('view_contact/<int:id>', views.view_contact, name='view_contact'),
    path('delete_contact/<int:id>', views.delete_contact, name='delete_contact'),




]

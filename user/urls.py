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

from django.urls import path,include
from.import views

urlpatterns = [
    path('home/',views.home, name='user-home'),
    path('login/',views.login, name='user_login'),
    path('user_logout/',views.user_logout, name='user_logout'),

    path('contact/', views.user_contact, name="contact"),
    path('user_profile/', views.user_profile, name="user_profile"),
    path('all_blog/', views.all_blog, name="all_blog"),
    path('single_blog/<int:id>/', views.single_blog, name="single_blog"),
    path('single_category/<str:name>/', views.single_category, name="single_category"),
    path('create_blog/', views.create_blog, name="create_blog"),
    path('user_profile/<str:username>/', views.user_profile, name="user_profile"),
    path('blog_list/', views.blog_list, name="user_blog_list"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),


]

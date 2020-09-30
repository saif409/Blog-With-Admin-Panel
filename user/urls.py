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
    path('register/',views.register, name='register'),
    path('user_logout/',views.user_logout, name='user_logout'),
    path('all_blog/', views.all_blog, name="all_blog"),
    path('single_blog/<int:id>/', views.single_blog, name="single_blog"),
    path('create_blog/', views.create_blog, name="create_blog"),
    path('user_profile/<int:id>', views.user_profile, name="user_profile"),
    path('edit_profile/<int:user_id>/', views.profile_edit, name="profile_edit"),
    path('blog_list/<int:user_id>/', views.blog_list, name="user_blog_list"),
    path('blog_remove/<int:id>/>', views.blog_remove, name="blog_remove"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),



]

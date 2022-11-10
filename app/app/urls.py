"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('register/', views.register),
    path('home/', views.home),
    path('subscribers/', views.subscribers),
    path('create-ticket/', views.create_ticket),
    path('answer-critic/', views.create_response_critic),
    path('new-critic/', views.create_new_critic),
    path('posts/', views.post),
    path('modify-critic/', views.modify_critic),
    path('modify-ticket/', views.modify_ticket),
]
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
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_page, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register/', views.register , name='register'),
    path('home/', views.home, name="home"),
    path('subscribers/', views.subscribers, name='following'),
    path('tickets/create/', views.create_ticket, name='ticket-create'),
    path('tickets/<int:id>/', views.ticket_details, name='ticket-detail'),
    path('tickets/<int:id>/update/', views.ticket_update, name='ticket-update'),
    path('answer-critic/', views.create_response_critic),
    path('new-critic/', views.create_new_critic),
    path('posts/', views.post, name='posts'),
    path('modify-critic/', views.critic_update),
    path('modify-ticket/', views.ticket_update),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
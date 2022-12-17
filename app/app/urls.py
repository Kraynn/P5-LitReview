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
    path('', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register/', views.register , name='register'),
    path('home/', views.home, name="home"),
    path('subscribers/', views.subscribe, name='sub'),
    path('subscribers/<id_user>/', views.unsubscribe, name='unsub'),  
    path('tickets/create/', views.create_ticket, name='ticket-create'),
    path('tickets/<int:id>/', views.ticket_details, name='ticket-detail'),
    path('tickets/<int:id>/update/', views.ticket_update, name='ticket-update'),
    path('ticket/delete/<int:id>', views.ticket_delete, name='ticket-delete'),
    path('review/delete/<int:id>', views.review_delete, name='review-delete'),
    path('review/<int:id>/update/', views.review_update, name='review-update'),
    path('ticket/<int:id>/review/create', views.create_ticket_review, name='new-review'),
    path('review/', views.create_review, name='review'),
    path('posts/', views.post, name='posts'),
    path('error/', views.error, name='error')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""flyMyTickets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from __future__ import unicode_literals
from django.contrib import admin
from django.conf.urls import url
from flyMeApp.views import UserCreateAPIView, BookingCreateAPIView, TicketCreateAPIView, BookingListAPIView, FlightListAPIView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
     url('admin/', admin.site.urls),
     url('signup/', UserCreateAPIView.as_view(), name='signup'),
     url('book/', BookingCreateAPIView.as_view(), name='booking'),
     url('create/flight', TicketCreateAPIView.as_view(), name='create-flight'),
     url('mybookings/', BookingListAPIView.as_view(), name='mybookings-list'),
     url('flights/', FlightListAPIView.as_view(), name='flights-list'),
     url('login/', TokenObtainPairView.as_view(), name='login'),
    
]


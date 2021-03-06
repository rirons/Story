"""djangolite URL Configuration

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
from django.contrib import admin
from django.urls import path
from .views import currentf,fcastedit,addroom,fcastall,testodbc
from .email import sendSimpleEmail




urlpatterns = [
    path('admin/', admin.site.urls),
    path('fcast',currentf),
    # path('fcast/<str:room>',fcastedit),
    path('fcast/all',fcastedit),
    path('fcast/add/',addroom),
    path('fcast-all',fcastall),
    path('sendmail',sendSimpleEmail),
    path('test',testodbc),
    path('test/<str:cname>',testodbc)

]

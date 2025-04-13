"""
URL configuration for demo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from sample import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("",views.index,name="index"),
    path("index",views.index,name="index"),
    path("about",views.about,name="about"),
    
    
    path("addData",views.addData,name="addData"),
    path("updateData/<int:id>",views.updateData,name="updateData"),
    path("deleteData/<int:id>",views.deleteData,name="deleteData"),
    path("register",views.register,name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout',views.logout,name="logout"),
    path('details',views.details,name="details"),
    path('contactt',views.contactt,name="contactt"),
    path('story',views.story,name="story"),
    path('services',views.services,name="services"),
    path('marriage',views.marriage,name="marriage"),
    path('traditional',views.traditional,name="traditional"),
    path('destination',views.destination,name="destination"),
    path('reception',views.reception,name="reception"),
    path('pubberty',views.pubberty,name="pubberty"),
    path('birthday',views.birthday,name="birthday"),
    path('admin_log',views.admin_log,name="admin_log"),
    
]

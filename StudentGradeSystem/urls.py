"""
URL configuration for StudentGradeSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from app import views


urlpatterns = [
    # 沒有prefix，直接進入app
    path('', views.getHomePage, name='home'),#! homePage 一定要在這邊？
    # 把app內的urls放入，prefix為app
    path("app/", include("app.urls")),


    path("authen/", include("authen.urls")) ,
    path("authen/", include("django.contrib.auth.urls")),#內建的authenication system
    #?, namespace="auth"

    path("admin/", admin.site.urls),

]

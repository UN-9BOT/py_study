"""
URL configuration for app project.

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
from typing import Callable
from django.contrib import admin
from django.http import HttpResponseNotFound
from django.urls import URLPattern, URLResolver, include, path

from quiz.views import page_not_found


urlpatterns: list[URLResolver | URLPattern] = [
    path("admin/", admin.site.urls),
    path("", include("quiz.urls"))
]

handler404: Callable[..., HttpResponseNotFound] = page_not_found

"""base_app URL Configuration

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
from django.views.static import serve
from django.urls import path, re_path, include

from seedcase.settings import DATA_FILE_URL, DATA_FILE_ROOT
from .views import home_page, organization_list, project_list
from .views import data_files

urlpatterns = [
    path("", home_page, name="home"),
    path("organizations/", organization_list, name="organizations"),
    path("projects/", project_list, name="projects"),
    path(DATA_FILE_URL, data_files, name="data_files"),
    re_path(r"^datafile/(?P<path>.*)$", serve, {"document_root": DATA_FILE_ROOT}),
]

# Add other apps url to the base app



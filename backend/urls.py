"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from db_course_work_backend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('guide/', admin.site.urls),
    path('excursions/', views.view_list_excursions),
    path('groups/', views.view_list_groups_tour),
    path('cg/', views.become_guide),
    path('crd/', views.register_become_random_dick),
    path('', views.default_page),
]

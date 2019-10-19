"""kpi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from webkpi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.positions, name='positions'),
    path('positions', views.positions, name='positions'),
    path('departments', views.departments, name='departments'),
    path('employees', views.employees, name='employees'),
    path('add_department/', views.add_department, name='add department'),
    path('departments/add', views.form_department, name='form departments'),
    path('add_employee/', views.add_employee, name='add employee'),
    path('employees/add', views.form_employees, name='form employees'),
    path('add_position/', views.add_position, name='add position'),
    path('positions/add', views.form_positions, name='form positions'),
]

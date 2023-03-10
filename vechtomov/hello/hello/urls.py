"""hello URL Configuration

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
from django.urls import re_path
from application import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('edit/<int:id>', views.edit),
    path('delete/<int:id>', views.delete),
    # path('about/', TemplateView.as_view(template_name="application/about.html")),
    # path('contact/', TemplateView.as_view(template_name="application/contact.html", extra_context={"work": "Разработка продуктов"})),
    # path('details/', views.to_start),
    # path('about/', views.about),
    # path('contact/', views.contact),
    # path('products/', views.products),
    # path('products/<int:productid>/', views.products),
    # path('users/<int:id>/<str:name>/', views.users),
    # path('users/', views.users),
    # path('admin/', admin.site.urls),
]

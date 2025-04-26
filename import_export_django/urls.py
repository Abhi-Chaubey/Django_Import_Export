"""
URL configuration for import_export_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from core.views import transform_data, home,import_file, export_output

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('import/', import_file, name='import_file'),
    path('transform_data/', transform_data, name='transform_data'),
    path('export_output/<str:format>/', export_output, name='export_output'),
]

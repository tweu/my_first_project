"""itc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django import urls
from course.views import branches_list, group_list, my_main_page, student_list
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from course.views import my_main_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/', include('course.urls')),
    path('', my_main_page, name = 'main_page'),
    path('user/', include('django.contrib.auth.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""lms URL Configuration

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
from django.urls import path, re_path

from students.views import get_students, create_student_view
from students.views import index

# from students.views import view_with_param
# from students.views import view_without_param

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('students/', get_students),
    path('students/create/', create_student_view),
    # path('test/route/param/', view_without_param),   #test/route/param/
    # path(re 'test/route/<str:value>/', view_with_param),   #test/route/df;lkjhrlkjgf's/

]

# \n    \t      \b


# https://  www.digitalocean.com   /community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-ru

# https://www.digitalocean.com/

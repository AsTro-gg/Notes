"""
URL configuration for notes project.

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
from base.views import home
from base.views import create_note,create_notecategory,edit_notecategory,edit_note,delete_notecategory,delete_note,register,loginpage,user_logout
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home , name = 'Homepage'),
    path('create-note/',create_note , name = 'create_note'),
    path('create-notecategory/', create_notecategory , name = 'create_notecategory'),
    path('edit-notecategory/<int:pk>/',edit_notecategory , name = 'edit_notecategory'),
    path('edit-note/<int:pk>/',edit_note, name='edit_note'),
    path('delete-notecategory/<int:pk>/',delete_notecategory,name= 'delete_notecategory'),
    path('delete-note/<int:pk>/', delete_note ,name='delete_note'),
    path('register/',register,name = 'register'),
    path('loginpage/',loginpage,name='loginpage'),
    path('logout/',user_logout,name ='logout')
]

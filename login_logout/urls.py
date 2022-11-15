"""third_project URL Configuration

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
from first_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage', views.show_data, name='homepage'),
    path('register', views.register_form, name='register'),
    path('user_login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('cookies-session', views.cookie_session),
    path('cookies-delete', views.cookie_delete),
    path('create-session',views.create_session),
    path('access-session', views.access_session),
    path('delete-session', views.delete_session),
]



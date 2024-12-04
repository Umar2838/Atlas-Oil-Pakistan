"""
URL configuration for myproject project.

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
from django.urls import path
from .views import index,login,submitcode,adminlogin,adminpanel,get_submitted_codes

urlpatterns = [
    path('', index ,name='index'), 
    path('login/',login, name='login'),
    path('submitcode/',submitcode, name='submitcode'),
    path('adminlogin/',adminlogin, name='adminlogin'),
    path('adminpanel/',adminpanel, name='adminpanel'),
path('api/get-submitted-codes/',get_submitted_codes, name='get_submitted_codes'),

]
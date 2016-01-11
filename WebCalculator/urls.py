"""WebCalculator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

import views


urlpatterns = [
    #root
    url(r'^$', views.api_root, name='api_root'),

    #functions
    url(r'^add/?$', views.add, name='add'),
    url(r'^multiply/?$', views.multiply, name='multiply'),
    url(r'^divide/?$', views.divide, name='divide'),
    url(r'^hello_world/$', views.hello_world, name='hello_world'),
    url(r'^asian_option/?$', views.asian_option, name='asian_option'),
    
    # url(r'^docs/', include('rest_framework_swagger.urls')),
]

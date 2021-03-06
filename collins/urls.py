"""collins URL Configuration

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
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from rest_framework.authtoken import views as restviews
from api.urls import router as api
from api.urls import job_results_router

import ui.urls
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/auth/', restviews.obtain_auth_token),
    url(r'^api/v1/', include(api.urls)),
    url(r'^api/v1/', include(job_results_router.urls)),
    url(r'^ui/', include(ui.urls)),
]

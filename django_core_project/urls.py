"""django_core_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin

from books import urls as books_urls
from django_core_project import settings
from . import views as project_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', project_views.index, name='index'),
    url(r'^hello/$', project_views.hello_world, name="hello_world"),
    url(r'^now/$', project_views.current_datetime, name="datetime_now"),
    url(r'^now/plus/(?P<hours_ahead>[\d]+)/$', project_views.ahead_datetime, name="datetime_ahead"),
    url(r'^request_meta/$', project_views.request_meta, name='request_meta'),
    url(r'^simple_form_handling/$', project_views.simple_form_handling, name='simple_form_handling'),
    url(r'^books/', include(books_urls)),
    url(r'^contact/$', project_views.contact_form, name='contact_form'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^debug/$', project_views.debug, name='debug'),
    ]

urlpatterns += [
    url(r'^', project_views.no_page, name="no_page"),
]
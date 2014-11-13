from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from app_login.views import main, signup


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'login.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app_login.views.main', name='main'),
    url(r'^signup$', 'app_login.views.signup', name='signup'),
    url(r'^signup$', 'app_login.views.signup', name='signup'),
    url(r'^login$', login, {'template_name': 'login.html', }, name="login"),
    url(r'^home$', 'app_login.views.home', name='home'),
    url(r'^logout$', logout, {'template_name': 'main.html', }, name="logout"),

)

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from app_login.views import main, signup
from userprofile.views import TodoList, TodoDetail, TodoCreate, TodoDelete, TodoUpdate, listar

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

    url(r'^$', 'userprofile.views.ingresar', name='ingresar'),
    url(r'^index$', TodoList.as_view(), name='app_list'),
    url(r'^Todo(?P<pk>\d+)$', TodoDetail.as_view(), name='app_detail'),
    url(r'^New$', TodoCreate.as_view(), name='app_create'),
    url(r'^Todo(?P<pk>\d+)/Update$', TodoUpdate.as_view(), name='app_update'),
    url(r'^Todo(?P<pk>\d+)/Delete$', TodoDelete.as_view(), name='app_delete'),
    url(r'^listar/todo$', 'userprofile.views.listar'),
    

)

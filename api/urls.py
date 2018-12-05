from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('registration', views.register),
    url('login', views.login),
    # path('', include('rest_auth.urls')),
    # path('registration/', include('rest_auth.registration.urls')),
    
    # url(r'^$', index),
    # url(r'^admin/', admin.site.urls),
    # # url(r'^login/$', views.login, {'template_name': 'login.html'}), 
    # url(r'^logout/$', views.logout, {'next_page': '/login'}),
    # url(r'^conversation$', broadcast),
    # url(r'^conversations/$', conversations),
    # url(r'^conversations/(?P<id>[-\w]+)/delivered$', views.delivered)
##add
]



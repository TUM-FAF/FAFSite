from django.conf.urls import patterns, include, url
from views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', index),
	url(r'^index/$', index),
	url(r'^about/$', about),
	url(r'^courses/Calculus-1/$', about_course),
	url(r'^courses/$', courses),
    url(r'^timeline/$', timeline),
    # Examples:
    # url(r'^$', 'fafsite.views.home', name='home'),
    # url(r'^fafsite/', include('fafsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import patterns, include, url
from views import *
from django.conf import settings
from filebrowser.sites import site


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', index),
	url(r'^index/$', index),
	url(r'^about/$', about),
	url(r'^admission/$', admission),
	url(r'^achievements/$', achievements),
	url(r'^activities/$', activities),
	url(r'^courses/Calculus-1/$', about_course),
	url(r'^courses/$', courses),
	url(r'^people/$', people),
	url(r'^contact-us/$', contact_us),
	url(r'^tinymce/', include('tinymce.urls')),
	# url(r'^admin/academics/user/add/$', 'admin_views.metakeys'),
	# Examples:
	# url(r'^$', 'fafsite.views.home', name='home'),
	# url(r'^fafsite/', include('fafsite.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^grappelli/', include('grappelli.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^admin/filebrowser/', include(site.urls)),
)


if settings.DEBUG:
	urlpatterns = patterns('',
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
	url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
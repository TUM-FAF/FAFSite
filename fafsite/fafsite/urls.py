from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from general.views import index, about, admission, thankyou
from academics.views import courses, about_course, professors, students, alumni
from fafemail.views import contact_us, thanks, sorry
from blog.views import achievements, activities


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^index/$', index),
    url(r'^about/$', about),
    url(r'^admission/$', admission),
    url(r'^achievements/$', achievements),
    url(r'^activities/$', activities),
    url(r'^courses/$', courses),
    url(r'^courses/([a-zA-Z-]+)/$', about_course),
    url(r'^people/$', professors),
    url(r'^people/professors/$', professors),
    url(r'^people/students/([a-zA-Z0-9]+)/$', students),
    url(r'^people/alumni/([a-zA-Z0-9]+)/$', alumni),
    url(r'^contact-us/$', contact_us),
    url(r'^contact-us/thanks/$', thanks),
    url(r'^contact-us/sorry/$', sorry),
    url(r'^thankyou/$', thankyou),
    url(r'^tinymce/', include('tinymce.urls')),
    # Admin panel and admin skin
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/filebrowser/', include(site.urls)),
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns

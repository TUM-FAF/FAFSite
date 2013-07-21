from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from general.views import index, about, admission, thankyou
from academics.views import courses, about_course, professors, students, alumni
from fafemail.views import contact_us, thanks, sorry
from blog.views import achievements, activities
from fafside.views import fafside_index, profile


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^index/$', index, name='index'),
    url(r'^about/$', about, name='about'),
    url(r'^admission/$', admission, name='admission'),
    url(r'^achievements/$', achievements, name='achievements'),
    url(r'^activities/$', activities, name='activities'),
    url(r'^courses/$', courses, name='courses'),
    url(r'^courses/([a-zA-Z-]+)/$', about_course, name='about_course'),
    url(r'^people/$', professors, name='people'),
    url(r'^people/professors/$', professors, name='professors'),
    url(r'^people/students/([a-zA-Z0-9]+)/$', students, name='students'),
    url(r'^people/alumni/([a-zA-Z0-9]+)/$', alumni, name='alumni'),
    url(r'^contact-us/$', contact_us, name='contact-us'),
    url(r'^contact-us/thanks/$', thanks, name='thanks'),
    url(r'^contact-us/sorry/$', sorry, name='sorry'),
    url(r'^thankyou/$', thankyou, name='thankyou'),
    # fafside - internal system urls
    url(r'^login/$', 'fafauth.views.authenticate', name='login'),
    url(r'^fafside/$', fafside_index, name='fafside_index'),
    url(r'^profile/$', profile, name='profile'),
    # url(r'^course_info_contribute/$', course_contrib, name='course_contrib'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'', include('social_auth.urls')),
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

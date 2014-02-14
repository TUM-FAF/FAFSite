from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from general.views import index, about, admission, thankyou
from academics.views import courses, about_course, professors, students, alumni
from fafemail.views import contact_us
from blog.views import achievements, activities, article
from fafauth.views import login_view, logout_view, register_view, passwordreset_view,
    passwordreset_initiated, passwordreset_success, passwordreset_confirm
from fafside.views import fafside_index, profile


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^index/$', index, name='index'),
    url(r'^$', index, name='index'),
    url(r'^about/$', about, name='about'),
    url(r'^admission/$', admission, name='admission'),
    url(r'^achievements/([0-9]+)/$', article, name='article'),
    url(r'^achievements/$', achievements, name='achievements'),
    url(r'^activities/([0-9]+)/$', article, name='article'),
    url(r'^activities/$', activities, name='activities'),
    url(r'^courses/$', courses, name='courses'),
    url(r'^courses/([a-zA-Z-]+)/$', about_course, name='about_course'),
    url(r'^people/$', professors, name='people'),
    url(r'^people/professors/$', professors, name='professors'),
    url(r'^people/students/([a-zA-Z0-9]+)/$', students, name='students'),
    url(r'^people/alumni/([a-zA-Z0-9]+)/$', alumni, name='alumni'),
    url(r'^contact-us/$', contact_us, name='contact-us'),
    url(r'^thankyou/$', thankyou, name='thankyou'),
    # authentication
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^register/$', register_view, name='register'),
    url(r'^passwordreset/$', passwordreset_view, name='passwordreset'),
    url(r'^passwordreset/initiated/$', passwordreset_initiated, name='passwordreset_initiated'),
    url(r'^passwordreset/success/$', passwordreset_success, name='passwordreset_success'),
    url(r'^passwordreset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', passwordreset_confirm, name='passwordreset_confirm'),
    # fafside - internal system urls
    url(r'^fafside/$', fafside_index, name='fafside_index'),
    url(r'^faflabs/$', 'faflabs.views.dashboard', name='faflabs_dashboard'),
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

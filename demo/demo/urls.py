from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'demo.views.home', name='home'),
    url(r'^dec/$', 'demo.views.dec', name='test'),
    url(r'^admin/', include(admin.site.urls)),
)

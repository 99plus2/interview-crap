from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shortener.views.home', name='home'),
    # url(r'^shortener/', include('shortener.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url('^$', 'shorten.views.new_url'),
    url('^link/(?P<key>[0-9A-Z]{5})$', 'shorten.views.view_shorten'),
    url('^goto/(?P<key>\w{5})$', 'shorten.views.do_redirect')
)

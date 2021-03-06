from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gmailstats.views.home', name='home'),
    # url(r'^gmailstats/', include('gmailstats.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^graph/', include('graphs.urls')), # ADD

    url(r'', include('social_auth.urls')),
    #url(r'^accounts/login/$',  login, name='login'),
    #url(r'^accounts/logout/$', logout, name='logout'),
)


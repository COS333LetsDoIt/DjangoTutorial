from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	# Examples:
	# these are URLconf's, which maps urls to views listed in views.py
	# url(r'^$', 'mysite.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	url(r'^polls/', include('polls.urls',  namespace='polls')), #namespace differentiates between different apps in the same project
	url(r'^admin/', include(admin.site.urls)),
)

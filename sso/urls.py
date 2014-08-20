from django.conf.urls import patterns, include, url
from django.contrib import admin
from mama_cas.views import LoginView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sso.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', 'sso.views.sso_login', name='sso_login'),
    url(r'^$', LoginView.as_view()),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('mama_cas.urls')),
)

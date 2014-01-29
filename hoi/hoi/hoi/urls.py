from django.conf.urls import *
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    # Examples:
    url(r'^admin/registry/persona/pdf/(?P<pk>\d+)/$', 'apps.registry.views.myview', name = 'pdf'),
    url(r'^admin/report$', 'apps.registry.views.report' , name = 'report'),
    url(r'^admin/report/error$', 'apps.registry.views.report_error' , name = 'error'),
    url(r'^admin/report/paises_global/$', 'apps.registry.views.paises_global', name = 'pais_global'),
    url(r'^admin/report/persona_genero/$', 'apps.registry.views.persona_genero', name = 'persona_genero'),
    # url(r'^hoi/', include('hoi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^favicon\.ico$','django.views.generic.simple.redirect_to',{'url': '/static/img/Ortopedico.jpg'}),
)

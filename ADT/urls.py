from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.SelectAppView.as_view(),name='select'),
    url(r'^(?P<pk>\d+)/claims/$',views.ClaimsView.as_view(),name='claims'),
    url(r'^(?P<pk>\d+)/One/$',views.OneView.as_view(),name='one'),
    url(r'^(?P<pk>\d+)/twelve/$',views.TwelveView.as_view(),name='twelve'),
    url(r'^(?P<pk>\d+)/art/$',views.ArtView.as_view(),name='art'),
    # url(r'^(?P<pk>\d+)/$', views.SpecificHomeView.as_view(), name='apphome'),

]
# if the DEBUG is on in settings, then append the urlpatterns as below
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

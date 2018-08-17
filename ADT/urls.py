from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.HomeView.as_view(),name='home'),
    url(r'^claims/$',views.ClaimsView.as_view(),name='claims'),
    url(r'^One/$',views.OneView.as_view(),name='one'),
    url(r'^twelve/$',views.TwelveView.as_view(),name='twelve'),
    url(r'^art/$',views.ArtView.as_view(),name='art'),

]
# if the DEBUG is on in settings, then append the urlpatterns as below
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

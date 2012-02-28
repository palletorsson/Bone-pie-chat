from django.conf.urls.defaults import patterns, url, include
from chat.api import v1  #tweets

from .views import IndexView, DetailView

urlpatterns = patterns('',
    url(r'^$',
        IndexView.as_view(),
        name='index'),

    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(),
        name="detail"),

    url(r'^api/', include(v1.urls)),
)



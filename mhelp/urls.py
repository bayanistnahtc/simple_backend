from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.schedule_list, name='schedule_list'),
    url(r'^download/(?P<file>.+)/$', views.download, name='download'), #^\d+-\d+-[1|2]

]
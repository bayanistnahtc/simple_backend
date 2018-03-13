from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.schedule_list, name='schedule_list'),
    url(r'^(?P<fac>[a-z]+)/(?P<pk>\d+-\d+-[1|2])/$', views.group_schedule, name='group_schedule'), #^\d+-\d+-[1|2]
]
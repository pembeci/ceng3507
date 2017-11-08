from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hello$', views.hello_page, name='somepage'),
    url(r'^hello/(?P<username>.+)/$', views.hello_page2, name='somepage'),
    url(r'^page2$', views.second, name='somepage'),
    url(r'^(?P<q_id>[0-9]+)/detail$', views.detail, name='detail_page'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),    
]

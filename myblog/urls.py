from django.conf.urls import url
from . import views

urlpatterns = [ 
	url(r'^$', views.mypost, name='mypost'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]
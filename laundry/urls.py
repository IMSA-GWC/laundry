from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home_page, name='home_page'),
    url(r'^(?P<hall>[1-7]{1})/$', views.hall_page, name = 'hall-laundry-page'),
	url(r'^user/new/$', views.user_new, name='user_new'),
	url(r'^user/login/$', views.user_login, name='user_login'),
	url(r'^user/error/$', views.user_error, name='user_error'),
	url(r'^user/logout/$', views.user_logout, name='user_logout'),
]

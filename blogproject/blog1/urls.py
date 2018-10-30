from django.conf.urls import url
from . import views
#视图函数命名空间
app_name='blog1'
urlpatterns = [
	url(r'^$',views.index,name='index'),
	#配置url的detail部分
	url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
	url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives,name='archives'),
	url(r'^category/(?P<pk>[0-9]+)/$',views.category,name='category')
]
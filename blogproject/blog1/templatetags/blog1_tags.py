from ..models import Post,Category
#注册为模板
from django import template
#获取数据库的前num篇文章
#实例化一个template.Library类
register=template.Library()
#并将get_recent_posts装饰为register.simple_tag
@register.simple_tag
def get_recent_posts(num=5):
	return Post.objects.all().order_by('-create_time')[:num]
@register.simple_tag
def archives():
	#dates函数的三个参数(创建时间字段，精确度，排序)
	return Post.objects.dates('create_time','month',order='DESC')
@register.simple_tag
def get_categories():
	return Category.objects.all()
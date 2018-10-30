# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible

#导入reverse函数
from django.urls import reverse

# Create your models here.
#Django要求模型必须继承models.Model类.
#CharField指定了分类名name的数据类型，CharField是字符型
#CharField的max_length参数指定最大长度，超过这个
#长度的分类名就不能存入数据库
#DateTimeField,IngeterField等等
@python_2_unicode_compatible
class Category(models.Model):
	#name是models.CharField的一个实例
	name=models.CharField(max_length=100)
	def __str__(self):
		return self.name
class Tag(models.Model):
	name=models.CharField(max_length=100)
	def __str__(self):
		return self.name
class Post(models.Model):
	#标题，正文，创建时间，修改时间，文章的摘要
	title=models.CharField(max_length=70)
	body=models.TextField()
	create_time=models.DateTimeField()
	modified_time=models.DateTimeField()
	excerpt=models.CharField(max_length=200,blank=True)
	# 我们在这里把文章对应的数据库表和分类、标签对应的数据库表关联了起来，但是关联形式稍微有点不同。
	# 一个分类下有多个文章，即一对多的关系
	# 一个文章有多个标签，一个标签下有多个文章，即多对多的关系
	category=models.ForeignKey(Category)
	tags=models.ManyToManyField(Tag,blank=True)
	#发表人
	#一个用户对应多篇文章，
	#django.contrib.auth.models.User，专门用于处理网站用户的注册，登录的流程
	author=models.ForeignKey(User)
	def __str__(self):
		return self.title
	#自定义get_absolute_url方法
	def get_absolute_url(self):
		#reverse中的'blog1:detail'对应urls文件的app_name='blog1'和name='detail'
		#kwargs里面就是一个键值对
		return reverse('blog1:detail',kwargs={'pk':self.pk})
	class meta:
		ordering = ['-create_time']

	

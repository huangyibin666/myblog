from django.shortcuts import render,get_object_or_404
import markdown

# Create your views here.
# 编写自己的视图函数
from django.http import HttpResponse
#表示的是从工程目录下去配置
from .models import Post,Category

#更新文章详情页的视图函数
from comments.forms import CommentForm

def index(request):
	#return HttpResponse('欢迎访问我的博客首页')
	#return render(request,'blog1/index.html',context={
		#'title':'我的博客首页',
		#'welcome':'欢迎访问我的博客首页'
		#})
	post_list=Post.objects.all().order_by('-create_time')
	return render(request,'blog1/index.html',context={
		'post_list':post_list
		})

def detail(request,pk):
	#django.shortcuts里面的get_object_or_404,传入Post的pk，如果pk在数据库中存在，则
	#返回对应的post，如果pk不存在，则返回404
	post = get_object_or_404(Post,pk=pk)
	post.body = markdown.markdown(post.body,
								  extensions=[
								  	 'markdown.extensions.extra',
								  	 'markdown.extensions.codehilite',
								  	 'markdown.extensions.toc',
								  ])
	form = CommentForm()
	#获取这篇post下的全部评论
	comment_list=post.comment_set.all()
	#将文章，表单以及文章下的评论列表作为模板变量传给detail.html模板
	context = {'post':post,
			   'form':form,
			   'comment_list':comment_list
			   }
	return render(request,'blog1/detail.html',context=context)
#通过归档获取归档下的全部文章
def archives(request,year,month):
	#filter筛选模板下的create_time的year和month属性，作为函数的参数列表
	post_list=Post.objects.filter(create_time__year=year,
								  create_time__month=month
								 )
	return render(request,'blog1/index.html',context={
		'post_list':post_list
		})
#通过分类获取分类下得全部文章
def category(request,pk):
	cate=get_object_or_404(Category,pk=pk)
	post_list=Post.objects.filter(category=cate).order_by('-create_time')
	return render(request,'blog1/index.html',context={
		'post_list':post_list
		})


	

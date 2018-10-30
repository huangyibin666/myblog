from django.shortcuts import render,get_object_or_404,redirect
from blog1.models import Post
from .models import Comment
from .forms import CommentForm
# Create your views here.
def post_comment(request,post_pk):
	#先获取被评论的文章
	post = get_object_or_404(Post,pk=post_pk)
	#Http请求一般有get和post两种
	if request.method == 'POST':
		#用户提交的数据存在request.POST中，这是一个类字典对象
		#我们利用这些数据构造CommentForm的实例，这样Django的表单就生成了
		form = CommentForm(request.POST)
		#调用form.is_valid()方法时，Django自动检查表单的数据是否符合格式要求
		if form.is_valid():
			#检查到数据是合法的，调用表单的save方法保存数据到数据库
			#commit=False的作用仅仅利用表单的数据生成Comment模型类的实例，但还不保存评论数据到数据库
			comment = form.save(commit=False)
			#将评论和被评论的文章关联起来
			comment.post = post
			#最终将评论和被评论的文章保存到数据库
			comment.save()
			#重定向到post的详情页，实际上当redirect函数接收一个模型的实例时，它会
			#调用这个模型实例的get_absolute_url
			#redirect必须接收一个url或实现了get_absolute_url的模型的实例
			return redirect(post)
		else:
			#这相当于方向查询
			#这里post.comment_set相当于Comment.objects.filter(post=post)
			#XXX_set,关联模型的小写
			comment_list=post.comment_set.all()
			context={'post':post,
					 'form':form,
					 'comment_list':comment_list
			        }
			return render(request,'blog1/detail.html',context=context)
	return redirect(post)

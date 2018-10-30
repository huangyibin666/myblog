from django.db import models
from django.utils.six import python_2_unicode_compatible


# Create your models here.
@python_2_unicode_compatible
class Comment(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=255)
	url = models.URLField(blank=True)
	text = models.TextField()
	#当评论提交自动把当前时间保存到数据库
	create_time = models.DateTimeField(auto_now_add=True)

	post=models.ForeignKey('blog1.Post')

	def __str__(self):
		return self.text[:20]

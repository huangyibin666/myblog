from django import forms
from .models import Comment
#导入forms模块，来使用Django的表单功能
#Django的表单必须继承forms.Form和forms.ModelForm
class CommentForm(forms.ModelForm):
	class Meta:
		#表单对应的数据库模型
		model = Comment
		#表单需要展示的字段
		fields = ['name','email','url','text']

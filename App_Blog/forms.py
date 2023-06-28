from django import forms
from .models import Blog
class CreateBlogPostForm(forms.ModelForm):
    blog_content=forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Blog
        fields = ['blog_title','catagory','blog_content','blog_image']
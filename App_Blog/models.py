from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogCatagory(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural="Catagories"

class Blog(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE,related_name="blog_author")
    catagory=models.ForeignKey(BlogCatagory, on_delete=models.CASCADE,related_name="category")
    blog_title=models.CharField(max_length=250,verbose_name="Put Blog Title")
    slug = models.SlugField(max_length = 250,unique=True,allow_unicode=True)
    blog_content=models.TextField(verbose_name="What is on your mind?")
    blog_image= models.ImageField(upload_to="blog_images", verbose_name="image",blank=True, null=True)
    publish_date=models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering=['-publish_date']
    def __str__(self):
        return self.blog_title
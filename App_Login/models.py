from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Teacher(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE,related_name="teacher")
    teacher_name = models.CharField(max_length = 250)
    teacher_image = models.ImageField(upload_to="teacher_image", verbose_name="Profile Picture",blank=True, null=True)
    teacher_designation = models.CharField(max_length = 10000000000000,blank=True, null=True)
    teacher_details = models.CharField(max_length = 10000000000000,blank=True, null=True)
    teacher_comment = models.CharField(max_length = 10000000000000,blank=True, null=True)

    def __str__(self):
        return self.teacher_name
    
    
    
    
    

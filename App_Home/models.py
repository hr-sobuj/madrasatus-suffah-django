from django.db import models

# Create your models here.
class Notice(models.Model):
    notice_title = models.CharField(max_length = 5000,verbose_name="Notice Title")
    notice_pdf = models.FileField(upload_to="notice_pdf", max_length = 254,verbose_name="Notice")
    publish_date=models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    

    class Meta:
        ordering=['-publish_date']

    def __str__(self):
        return self.notice_title
    

class Gallery(models.Model):
    caption = models.CharField(max_length = 10000000000000,verbose_name="Caption")
    image = models.ImageField(upload_to="gallery",verbose_name="Image")
    publish_date=models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering=['-publish_date']

    def __str__(self):
        return self.caption
    


    
    
    

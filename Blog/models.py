from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Post(models.Model):
 title = models.CharField(max_length=150)
 category = models.CharField(max_length=60)
 tags = models.CharField(max_length=550, default='')
 desc = models.TextField()
 date = models.DateTimeField(auto_now_add=True )
 image = models.ImageField(upload_to='posts/%Y/%m/%d',blank=True , default='posts\default\default.jpg')
 user_id = models.ForeignKey(User, on_delete=models.CASCADE , default='1')


 def delete(self , *args , **kwargs):
     self.image.delete()
     super().delete(*args , **kwargs)



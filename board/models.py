from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목')
    user = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE, null= True)
    description = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True)



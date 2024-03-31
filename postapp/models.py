# models.py

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # 画像フィールドを追加
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

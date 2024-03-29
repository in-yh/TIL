from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10) # 11자면 유효성검사에서 False
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

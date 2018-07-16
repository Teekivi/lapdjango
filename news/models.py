from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    author = models.ForeignKey(User, on_delete=models.PROTECT, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

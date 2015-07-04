#! coding=utf-8
# coding=utf-8
from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)  # 博客题目
    category = models.CharField(max_length=50, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    # 按时间下降排序
    class Meta:
        ordering = ['-date_time']




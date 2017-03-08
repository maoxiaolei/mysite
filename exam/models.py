#_*_coding:utf-8_*_
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.TextField('题目',max_length=500)
    pub_date = models.DateTimeField('日期')
    choices = (
        (1,'单选题'),
        (2,'多选题'),
        (3,'判断题'),
        (4,'简答题')
    )
    question_class = models.SmallIntegerField('题目类型',choices=choices)

    class Meta:
        permissions = (
            ("view_task", "Can see available tasks"),
            ("change_task_status", "Can change the status of tasks"),
            ("close_task", "Can remove a task by setting its status as closed"),
        )

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    abc = models.CharField(max_length=10,null=True)
    choice_text = models.CharField('选项',max_length=500)
    correct_choice = models.BooleanField('正确答案',default=False)

class Content(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content_text = models.TextField('答案',max_length=2000)
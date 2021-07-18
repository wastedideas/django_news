from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class New(models.Model):
    active_choices = [
        (True, 'Активаная'),
        (False, 'Неактивная'),
    ]

    new_name = models.CharField(
        max_length=100,
        verbose_name='Новость',
    )
    new_desc = models.CharField(
        max_length=1000,
        verbose_name='Описание',
    )
    new_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    new_edit = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата редактирования',
    )
    new_active_flag = models.BooleanField(
        choices=active_choices,
        default=False,
        verbose_name='Активность новости',
    )

    def __str__(self):
        return self.new_name


class Comment(models.Model):
    user_name = models.CharField(
        max_length=20,
        verbose_name='Имя пользователя',
    )
    comment_text = models.TextField(
        max_length=1000,
        verbose_name='Комментарий',
    )
    new = models.ForeignKey(
        'New',
        default=None,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Новость',
    )
    user = models.ForeignKey(
        User,
        default=None,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )

    def __str__(self):
        return self.short_comment()

    @admin.display(description='Комментарий')
    def short_comment(self):
        if len(str(self.comment_text)) > 15:
            return f'{self.comment_text[:15]}...'
        else:
            return self.comment_text

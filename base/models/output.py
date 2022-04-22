from django.db import models
from django.contrib.auth import get_user_model

class Output(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    question = models.TextField(
        verbose_name='質問',
        null=True,
        blank=True,
    )

    description = models.TextField(
        verbose_name='内容'
    )

    created_at = models.DateTimeField(
        verbose_name = '投稿日',
        auto_now_add = True,
    )

    updated_at = models.DateTimeField(
        verbose_name = '更新日',
        auto_now = True
    )

    def __str__(self):
        return self.description[:10]
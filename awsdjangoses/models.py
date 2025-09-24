from django.db import models


class AwsBlackList(models.Model):
    email = models.EmailField(max_length=500, primary_key=True)
    bounce = models.BooleanField(default=False)
    complaint = models.BooleanField(default=False)


class AwsDelivery(models.Model):
    mail = models.JSONField(default=dict, blank=True)
    delivery = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания",
        db_index=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Время последнего изменения",
        db_index=True,
    )

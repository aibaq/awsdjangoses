from django.db import models


class AwsBlackList(models.Model):
    email = models.EmailField(max_length=500, primary_key=True)
    bounce = models.BooleanField(default=False)
    complaint = models.BooleanField(default=False)

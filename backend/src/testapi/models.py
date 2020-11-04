from django.db import models
from django.conf import settings


class Project(models.Model):
    """
        QA Project Model
    """

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='leader')
    name = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    people = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='team')
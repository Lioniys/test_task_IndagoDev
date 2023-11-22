from django.db import models
from django.conf import settings


class Notes(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=5000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'user - {self.user} product - {self.title}'

    class Meta:
        ordering = ['id']

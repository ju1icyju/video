from django.db import models


class PageRequest(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.text

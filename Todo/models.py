from django.db import models
from django.urls import reverse

# Create your models here.
class Todolist(models.Model):
    title = models.TextField(blank=True, null=True)
    finish = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("list_detail", args=[str(self.id)])




from django.db import models

# Create your models here.
class Product(models.Model):
    def __str__(self) -> str:
        return self.title
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()
    summary = models.TextField(default='this is cool!')
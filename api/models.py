from django.db import models
import uuid

# Create your models here.
class ServiseProvide(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, unique=True, verbose_name="Name")
    post = models.CharField(max_length=300, verbose_name="Post")
    phone = models.IntegerField()

    def __str__(self):
        return self.post

class Clients(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, unique=True, verbose_name="Name")
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name
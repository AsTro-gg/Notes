from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class NoteCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Note(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(NoteCategory, on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
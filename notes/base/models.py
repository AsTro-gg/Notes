from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class NoteCategory(models.Model):
    name = models.CharField(max_length=100)

class Note(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(NoteCategory, on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)

class gukha(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Note,on_delete=models.SET_NULL,null=True)
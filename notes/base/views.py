from django.shortcuts import render
from django.http import HttpResponse
from .models import Note

# Create your views here.

def home(request):
    note_objs = Note.objects.all()
    data  = {'notes':note_objs}
    return render(request,'index.html',context=data)
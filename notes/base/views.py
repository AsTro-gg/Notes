from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Note
from .models import NoteCategory
from .forms import NoteCategoryForm
from .forms import NoteForm

# Create your views here.

def home(request):
    note_objs = Note.objects.all().order_by('id')
    notecategory_objs = NoteCategory.objects.all().order_by('id')
    data  = {'notes':note_objs,'notecategories':notecategory_objs}
    return render(request,'index.html',context=data)
    
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
    form = NoteForm
    data = {'form':form}
    return render(request,'create_note.html',context=data)
    

def create_notecategory(request):
    if request.method == 'POST':
        form = NoteCategoryForm(request.POST)
        if form.is_valid():
            form.save()
    form = NoteCategoryForm
    data = {'form':form}
    return render(request,'create_notecategory.html',context=data)

def edit_notecategory(request,pk):
    note_category_obj =NoteCategory.objects.get(id=pk)
    if request.method == 'POST':
        form = NoteCategoryForm(request.POST,instance=note_category_obj)
        if form.is_valid():
            form.save()
    form = NoteCategoryForm(instance=note_category_obj)
    data = {'form':form}
    return render(request,'edit_notecategory.html',context=data)

def edit_note(request,pk):
    note_obj = Note.objects.get(id=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST,instance=note_obj)
        if form.is_valid():
            form.save()
    form = NoteForm(instance=note_obj)
    data = {'form':form}
    return render(request,'edit_note.html',context=data)

def delete_notecategory(request,pk):
    notecategory = NoteCategory.objects.get(id=pk)
    notecategory.delete()
    return redirect('Homepage')
        
def delete_note(request,pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return redirect('Homepage')
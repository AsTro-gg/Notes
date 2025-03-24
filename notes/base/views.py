from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
from .models import NoteCategory
from .forms import NoteCategoryForm

# Create your views here.

def home(request):
    note_objs = Note.objects.all()
    notecategory_objs = NoteCategory.objects.all()
    data  = {'notes':note_objs,'notecategories':notecategory_objs}
    return render(request,'index.html',context=data)
    
def create_note(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category_id= request.POST.get('category')
        notecategory_obj = NoteCategory.objects.get(id=category_id) # This is a relation field so, we import its id.

        Note.objects.create(name=name,description=description,category=notecategory_obj)
    note_category = NoteCategory.objects.all()
    notecategory_data = {'categories': note_category}
    return render(request,'create_note.html',context=notecategory_data)

def create_notecategory(request):
    if request.method == 'POST':
        form = NoteCategoryForm(request.POST)
        if form.is_valid():
            form.save()
    form = NoteCategoryForm
    data = {'form':form}
    return render(request,'create_notecategory.html',context=data)

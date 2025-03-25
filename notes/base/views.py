from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Note
from .models import NoteCategory
from .forms import NoteCategoryForm
from .forms import NoteForm
from .forms import Userform
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        note_objs = Note.objects.all().order_by('id')
        notecategory_objs = NoteCategory.objects.all().order_by('id')
        data  = {'notes':note_objs,'notecategories':notecategory_objs}
        return render(request,'index.html',context=data)
    else:
        return redirect('loginpage')
    
def create_note(request):
    if request.user.is_authenticated:        
        if request.method == 'POST':
            form = NoteForm(request.POST)
            if form.is_valid():
                form.save()
        form = NoteForm
        data = {'form':form}
        return render(request,'create_note.html',context=data)
    else:
        return redirect('loginpage')    

def create_notecategory(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = NoteCategoryForm(request.POST)
            if form.is_valid():
                form.save()
        form = NoteCategoryForm
        data = {'form':form}
        return render(request,'create_notecategory.html',context=data)
    else:
        return redirect('loginpage')
    
def edit_notecategory(request,pk):
    if request.user.is_authenticated:
        note_category_obj =NoteCategory.objects.get(id=pk)
        if request.method == 'POST':
            form = NoteCategoryForm(request.POST,instance=note_category_obj)
            if form.is_valid():
                form.save()
        form = NoteCategoryForm(instance=note_category_obj)
        data = {'form':form}
        return render(request,'edit_notecategory.html',context=data)
    else:
        return redirect('loginpage')
    
def edit_note(request,pk):
    if request.user.is_authenticated:
        note_obj = Note.objects.get(id=pk)
        if request.method == 'POST':
            form = NoteForm(request.POST,instance=note_obj)
            if form.is_valid():
                form.save()
        form = NoteForm(instance=note_obj)
        data = {'form':form}
        return render(request,'edit_note.html',context=data)
    else:
        return redirect('loginpage')
    
def delete_notecategory(request,pk):
    if request.user.is_authenticated:
        notecategory = NoteCategory.objects.get(id=pk)
        notecategory.delete()
        return redirect('Homepage')
    else:
        return redirect('loginpage')
            
def delete_note(request,pk):
    if request.user.is_authenticated:
        note = Note.objects.get(id=pk)
        note.delete()
        return redirect('Homepage')
    else:
        return redirect('loginpage')

def register(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        encrypted = make_password(password)
        data = request.POST.copy()
        data['password'] = encrypted
        form = Userform(data)
        if form.is_valid():
            form.save()
        else:
            return render(request,'register.html',{'form':form})
    form = Userform()
    data = {'form':form}
    return render(request,'register.html',context=data)

def loginpage(request):
    form = Userform()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user == None:
            return render(request,'login.html',context={'form':form,'error':'Invalid username or password'})
        else:
            login(request,user)
            return redirect('Homepage')
    form = Userform()
    data = {'form':form}
    return render(request,'login.html',context=data)

def user_logout(request):
    logout(request)
    return redirect('loginpage')
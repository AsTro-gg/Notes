from django import forms
from .models import NoteCategory
from .models import Note
from django.contrib.auth.models import User

class NoteCategoryForm(forms.ModelForm):
    class Meta:
        model = NoteCategory
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control' } )
        }


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields =['name','description','category']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-select'})
        }

class Userform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'})
            }
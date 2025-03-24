from django import forms
from .models import NoteCategory
from .models import Note

class NoteCategoryForm(forms.ModelForm):
    class Meta:
        model = NoteCategory
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'})
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

    
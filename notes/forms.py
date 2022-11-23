from django import forms
from .models import Notes
from django.core.exceptions import ValidationError


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'note']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-2'}),
            'note': forms.Textarea(attrs={'class': 'form-control my-2'})
        }
        labels = {
            'note': 'Write your note here:'
        }
    
    def clean_note(self):
        note = self.cleaned_data['note']
        if 'Django' not in note:
            raise ValidationError('We only accept notes about Django!')
        return note

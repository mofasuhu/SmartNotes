from django.http import HttpResponseRedirect
from .models import Notes
from .forms import NotesForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class NoteDeleteView(DeleteView):
    template_name = 'notes/notes_delete.html' 
    model = Notes
    context_object_name = 'note'
    success_url = '/smart/notes/'

class NoteUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes/'
    form_class = NotesForm    

class NoteCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes/'
    form_class = NotesForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    login_url = 'login'
    
    def get_queryset(self):
        return self.request.user.notes.all()
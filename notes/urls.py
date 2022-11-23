from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.NotesListView.as_view(), name='notes.list'),
    path('notes/<int:pk>/', views.NotesDetailView.as_view(), name='note.detail'),
    path('notes/new/', views.NoteCreateView.as_view(), name='note.new'),
    path('notes/<int:pk>/update/', views.NoteUpdateView.as_view(), name='note.update'),
   path('notes/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='note.delete'),
]
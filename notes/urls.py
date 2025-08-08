from django.urls import path
from .views import NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView

urlpatterns = [
    path('', NoteListView.as_view(), name='note-list'),
    path('create/', NoteCreateView.as_view(), name='note-create'),
    path('<int:pk>/edit/', NoteUpdateView.as_view(), name='note-edit'),
    path('<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
]
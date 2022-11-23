from django.contrib import admin
from . import models

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'note', 'created', 'user_id')

admin.site.register(models.Notes, NotesAdmin)


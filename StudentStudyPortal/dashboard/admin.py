from django.contrib import admin
from .models import Notes,Homework, Todo
# Register your models here.
@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ['user','title','description']

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ['user','subject','title','description','due','is_finished']

@admin.register(Todo)
class Todo(admin.ModelAdmin):
    list_display = ['user','title','is_finished']
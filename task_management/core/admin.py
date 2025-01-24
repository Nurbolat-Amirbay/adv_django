from django.contrib import admin 
from .models import Task, Project 

@admin.register(Task) 

class TaskAdmin(admin.ModelAdmin): 

    list_display = ('title', 'project', 'due_date') 

    search_fields = ('title',) 

 
@admin.register(Project) 

class ProjectAdmin(admin.ModelAdmin): 

    list_display = ('name', 'start_date', 'end_date') 
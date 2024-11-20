from django.contrib import admin
from .models import ProgrammingQuestion

@admin.register(ProgrammingQuestion)
class ProgrammingQuestionAdmin(admin.ModelAdmin):
    list_display = ('sr_no', 'question', 'language')  # Fields to display in the admin list view

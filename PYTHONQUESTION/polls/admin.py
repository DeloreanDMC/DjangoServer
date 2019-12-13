from django.contrib import admin
from .models import Question, Answer

# Register your models here.
class AnswerInline(admin.StackedInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
    (None,
    {'fields': ['title', 'owner']}
    ),
    ('Информация о дате',
    {'fields': ['date_publish'],
    'classes': ['collapse']}
    ),
    ]
    inlines = [AnswerInline]


admin.site.register(Question, QuestionAdmin)
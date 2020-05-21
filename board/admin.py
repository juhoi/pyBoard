from django.contrib import admin
from .models import Question, Answer


# Register your models here.
# class AnswerInline(admin.StackedInline):
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'content', 'create_date')
    search_fields = ['subject']
    inlines = [AnswerInline]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'content', 'create_date')
    search_fields = ['question']

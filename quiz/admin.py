from django.contrib import admin

from . import models

@admin.register(models.Category)
class Category_Admin(admin.ModelAdmin):
    list_display = [
        'title',
    ]


@admin.register(models.Quiz)
class Quiz_Admin(admin.ModelAdmin):
    list_display = [
        'id',
        'quiz_title',
    ]



class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    list_display = [
        'answer_text',
        'is_correct',
    ]


@admin.register(models.Question)
class Question_Admin(admin.ModelAdmin):
    fields = [
        'quiz_title',
        'quiz'
    ]
    list_display = [
        'quiz_title',
        'quiz',
        'created_at',

    ]

    inlines = [
        AnswerInlineModel,
    ]

@admin.register(models.Answer)
class Answer_Admin(admin.ModelAdmin):
    list_display = [
        'answer_text',
        'is_correct',
        'question',
    ]
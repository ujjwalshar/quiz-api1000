from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext as _

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Quiz(models.Model):
    category = models.ForeignKey(Category, default=1, on_delete=models.PROTECT)
    quiz_title = models.CharField(max_length=255, default=_('New Quiz'), verbose_name=_('Quiz Title'))
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    class Meta:
        verbose_name = _('Quiz')
        verbose_name_plural = _('Quizzes')
        ordering = ['id']

    def __str__(self):
        return self.quiz_title

    

class UpdatedQuestion(models.Model):
    updated_date = models.DateTimeField(verbose_name=_('Last Updated'), auto_now=True)

    class Meta:
        abstract = True


class Question(UpdatedQuestion):
    quiz = models.ForeignKey(Quiz, related_name='question', on_delete=models.PROTECT)
    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
        ordering = ['id']

    Difficulty = (
        (0, _('Beginner')),
        (1, _('Intermediate')),
        (2, _('Advanced')),
        (3, _('Expert'))

    )

    Type = (
        (0, _('Multiple choice')),
        (1, _('Open Text'))

    )

    types = models.IntegerField(choices=Type, default=0, verbose_name=_('Type of Question'))
    difficulty = models.IntegerField(choices=Difficulty, default=0, verbose_name=_('Difficulty Level'))
    quiz = models.ForeignKey(Quiz, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Date Created'))
    is_active = models.BooleanField(default=False, verbose_name=_('Status is Active'))
    quiz_title = models.CharField(max_length=255, verbose_name=_('Title'))

    def __str__(self):
        return self.quiz_title


class Answer(UpdatedQuestion):
    question = models.ForeignKey(Question, related_name='Answer', on_delete=models.PROTECT)
    answer_text = models.CharField(max_length=255, verbose_name=_('Answer Text'))
    is_correct = models.BooleanField(default=False)
    class Meta:
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')
        ordering = ['id']

    def __str__(self):
        return self.answer_text
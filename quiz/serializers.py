from dataclasses import field, fields
from operator import mod
from pyexpat import model
from rest_framework import serializers
from .models import Answer, Quiz, Question


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = [
            'quiz_title'
        ]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_correct',
        ]

class RandomQuestionSerializer(serializers.ModelSerializer):

    Answer = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = [
            'quiz_title',
            'Answer',
        ]


class QuestionSerializer(serializers.ModelSerializer):
    
    
    Answer = AnswerSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True)
    class Meta:
        model = Question
        fields = [
            'quiz',
            'quiz_title',
            'Answer',
        ]
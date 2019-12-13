from rest_framework import serializers
from polls.models import Question
from polls.models import Answer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('title', 'date_publish','owner')

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('question','answer','votes')
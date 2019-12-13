from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    """
        СУЩНОСТЬ ВОПРОС:
        - вопрос
        - дата публикации
        - кто задал вопрос (никнейм)
    """
    title = models.CharField('Вопрос', max_length = 256)
    date_publish = models.DateTimeField('Дата публикации')
    owner = models.CharField('Кто задал (Ник)', max_length = 256)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Вопрос"
        verbose_name_plural="Вопросы"

class Answer(models.Model):
    """
        СУЩНОСТЬ ОТВЕТ:
        - сам вопрос
        - ответ 
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField('Ответ', max_length=256)
    votes = models.IntegerField('Голосов', default=0)
    
    def __str__(self):
        return self.answer

    class Meta:
        verbose_name="Ответ"
        verbose_name_plural="Ответы"
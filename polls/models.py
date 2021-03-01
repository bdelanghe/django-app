from datetime import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text: str = models.CharField(max_length=200)
    pub_date: datetime = models.DateTimeField('date published')

    def __str__(self) -> str:
        return self.question_text

    def was_published_recently(self) -> bool:
        recent: bool = (self.pub_date >= timezone.now())
        return recent

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text: str = models.CharField(max_length=200)
    votes: int = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
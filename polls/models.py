from datetime import datetime
from typing import Final, final
from django.db.models import Field

from django.db import models
from django.utils import timezone

# Create your models here.

_MAX_LENGTH: Final = 200

@final
class Question(models.Model):
    question_text: Field[str, str] = models.CharField(max_length=_MAX_LENGTH)
    pub_date: Field[datetime, datetime] = models.DateTimeField('date published')

    def __str__(self) -> str:
        return self.question_text

    def was_published_recently(self) -> bool:
        recent: bool = (self.pub_date >= timezone.now())
        return recent

@final
class Choice(models.Model):
    question: Field[str, str] = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text: Field[str, str] = models.CharField(max_length=_MAX_LENGTH)
    votes: Field[int, int] = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
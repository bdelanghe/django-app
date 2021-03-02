import datetime
from typing import Final, final

from django.db import models
from django.utils import timezone

# Create your models here.

_MAX_LENGTH: Final = 200
_STARTING_VOTES: Final = 0
_DAYS_OLD_RECENT: Final = 1


@final
class Question(models.Model):
    question_text = models.CharField(max_length=_MAX_LENGTH)
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.question_text

    def was_published_recently(self) -> bool:
        return self.pub_date >= timezone.now() - datetime.timedelta(days=_DAYS_OLD_RECENT)



@final
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=_MAX_LENGTH)
    votes = models.IntegerField(default=_STARTING_VOTES)

    def __str__(self) -> str:
        return self.choice_text

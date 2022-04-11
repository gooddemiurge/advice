from django.db import models

# Create your models here.

class Answer(models.Model):
    text = models.TextField("Відповідь")
    author = models.CharField("Автор", max_length=30)
    date = models.DateField()

    def __str__(self):
        return self.text

class Post(models.Model):

    question = models.TextField("Питання")
    author = models.CharField("Автор", max_length=30)
    answers = Answer()
    isClosed = models.BooleanField("Cтатус")
    date = models.DateField()

    def __str__(self):
        return self.question

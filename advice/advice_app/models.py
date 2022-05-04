from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Answer(models.Model):
    text = models.TextField("Відповідь")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    rating = models.IntegerField()

    def __str__(self):
        return self.text

class Post(models.Model):
    title = models.CharField("Заголовок", max_length=50)
    question = models.TextField("Питання")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    answers = models.ManyToManyField(Answer)
    isClosed = models.BooleanField("Cтатус")
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.question


class My_user(User):
    rating = models.IntegerField()

    def __str__(self):
        return self.rating

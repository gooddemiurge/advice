from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField("Заголовок", max_length=50)
    question = models.TextField("Питання")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    isClosed = models.BooleanField("Cтатус")
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.question

class Answer(models.Model):
    text = models.TextField("Відповідь")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name="answers")
    date = models.DateField(auto_now=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.text


class My_user(User):
    rating = models.IntegerField()

    def __str__(self):
        return self.rating

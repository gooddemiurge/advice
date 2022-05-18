from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.shortcuts import redirect
from django.urls import reverse


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=50)
    question = models.TextField("Питання")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    isClosed = models.BooleanField("Cтатус", default=0)
    date = models.DateField(auto_now=True)

    def get_absolute_url(self, **kwargs):
        return reverse('detail', kwargs={'pk':self.id})

    def __str__(self):
        return self.question

class Answer(models.Model):
    text = models.TextField("Відповідь")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name="answers")
    date = models.DateField(auto_now=True)
    rating = models.IntegerField(default=0)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.text


class My_user(User):
    rating = models.IntegerField()

    def __str__(self):
        return self.rating

class Key_words(models.Model):
    posts = models.ManyToManyField(Post)
    word = models.TextField(max_length=50)

    def __str__(self):
        return self.word

    @staticmethod
    def is_key_word(word):
        if len(word) > 1 and " " not in word or word.isdigit():
            return True
        else:
            return False

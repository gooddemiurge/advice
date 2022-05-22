from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class MyUser(User):
    """
    Model MyUser inherited from django.contrib.auth.model User.

    Model contains extra field rating.
    """
    class Meta:
        verbose_name = u"Рейтинг"
    rating = models.IntegerField("User", default=0)

    def __str__(self):
        return self.username

class Post(models.Model):
    """Post model."""
    title = models.CharField("Заголовок", max_length=50)
    question = models.TextField("Питання")
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    isClosed = models.BooleanField("Cтатус", default=0)
    date = models.DateField(auto_now=True)


    def get_absolute_url(self, **kwargs):
        return reverse('detail', kwargs={'pk':self.id})

    def __str__(self):
        return self.question


class Answer(models.Model):
    """Answer model."""
    text = models.TextField("Відповідь")
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name="answers")
    date = models.DateField(auto_now=True)
    rating = models.IntegerField(default=0)
    users_increased_rating = models.ManyToManyField(MyUser, related_name="users_increased_rating")
    users_decreased_rating = models.ManyToManyField(MyUser, related_name="users_decreased_rating")

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.text


class KeyWords(models.Model):
    """
    Keywords model.

    This model is related to the Post model and contains three methods for work with keyword search.
    """
    posts = models.ManyToManyField(Post)
    word = models.TextField(max_length=50)

    def __str__(self):
        return self.word

    @staticmethod
    def is_key_word(text):
        """Сhecks if the word is a keyword."""
        isKeyword = len(text) > 1 and " " not in text or text.isdigit()
        return isKeyword

    @staticmethod
    def remove_punctuation(text):
        """Removes punctuation for correct search function work."""
        text = text.replace(".", "").replace(",", "").replace("?", "").replace("!", "").replace(":", "").replace(";", "")
        return text

    @staticmethod
    def translate(text):
        """
        Solves the problem of changing the layout by replacing the Latin alphabet with Cyrillic.
        """
        incorrect_input_dict = {
            "q":"й", "w":"ц", "e":"у", "r":"к", "t":"е", "y":"н", "u":"г", "i":"ш", "o":"щ", "p":"з", '[':"х",
            "]":"ї", "a":"ф", "s":"і", "d":"в", "f":"а", "g":"п", "h":"р", "j":"о", "k":"л", "l":"д", ";":"ж",
            "'":"є", "z":"я", "x":"ч", "c":"с", "v":"м", "b":"и", "n":"т", "m":"ь", ",":"б", ".":"ю", "`":"'",
            "Q":"Й", "W":"Ц", "E":"У", "R":"К", "T":"Е", "Y":"Н", "U":"Г", "I":"Ш", "O":"Щ", "P":"З", '{':"Х",
            "}":"Ї", "A":"Ф", "S":"І", "D":"В", "F":"А", "G":"П", "H":"Р", "J":"О", "K":"Л", "L":"Д", ":":"Ж",
            '"':"Є", "Z":"Я", "X":"Ч", "C":"С", "V":"М", "B":"И", "N":"Т", "M":"Ь", "<":"Б", ">":"Ю", "~":"'"
        }
        new_text = ""
        for letter in text:
            if letter in incorrect_input_dict.keys():
                new_text += incorrect_input_dict[letter]
            else:
                new_text += letter

        return new_text

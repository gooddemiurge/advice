from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Post, Answer
from django.forms import ModelForm, Textarea, TextInput


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "question", "isClosed"]
        widgets ={
            "title": TextInput(attrs={'placeholder': 'Введіть заголовок', 'class': 'form-control'}),
            "question": Textarea(attrs={'placeholder': 'Введіть питання', 'class': 'form-control'})
        }

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ["text"]
        widgets = {"text": Textarea(attrs={'placeholder': 'Додайте відповідь', 'rows':5, 'cols':146, 'class': 'form-control'})}

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({'class':'form-control', 'placeholder':"Введіть iм'я користувача"})
        self.fields["password1"].widget.attrs.update({'class': 'form-control', 'placeholder': "Введіть пароль"})
        self.fields["password2"].widget.attrs.update({'class': 'form-control', 'placeholder': "Підтвердіть пароль"})

    class Meta:
        model = User
        fields = ["username", 'password1', 'password2']

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({'class':'form-control', 'placeholder':"Введіть iм'я користувача"})
        self.fields["password"].widget.attrs.update({'class': 'form-control', 'placeholder': "Введіть пароль"})

    class Meta:
        model = User
        fields = ["username", 'password']
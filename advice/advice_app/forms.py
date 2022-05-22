from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Post, Answer, MyUser
from django.forms import ModelForm, Textarea, TextInput


class PostForm(ModelForm):
    """Form for adding posts."""
    class Meta:
        model = Post
        fields = ["title", "question"]
        widgets ={
            "title": TextInput(attrs={'placeholder': 'Введіть заголовок', 'class': 'form-control'}),
            "question": Textarea(attrs={'placeholder': 'Введіть питання', 'class': 'form-control'})
        }

class AnswerForm(ModelForm):
    """Form for adding answer."""
    class Meta:
        model = Answer
        fields = ["text"]
        widgets = {"text": Textarea(attrs={'placeholder': 'Додайте відповідь', 'rows':5, 'cols':146, 'class': 'form-control'})}

class SignUpForm(UserCreationForm):
    """
    Creating account form, inherited from Django UserCreationForm.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({'class':'form-control', 'placeholder':"Введіть iм'я користувача"})
        self.fields["password1"].widget.attrs.update({'class': 'form-control', 'placeholder': "Введіть пароль"})
        self.fields["password2"].widget.attrs.update({'class': 'form-control', 'placeholder': "Підтвердіть пароль"})

    class Meta:
        model = MyUser
        fields = ["username", 'password1', 'password2']

class LoginForm(AuthenticationForm):
    """
    Authentication form, inherited from Django AuthenticationForm.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({'class':'form-control', 'placeholder':"Введіть iм'я користувача"})
        self.fields["password"].widget.attrs.update({'class': 'form-control', 'placeholder': "Введіть пароль"})

    class Meta:
        model = MyUser
        fields = ["username", 'password']
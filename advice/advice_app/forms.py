from .models import Post, Answer
from django.forms import ModelForm, Textarea

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "question", "isClosed"]
        widgets = {"question": Textarea(attrs={'placeholder': 'Введіть питання'})}

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ["text", "rating"]
        widgets = {"text": Textarea(attrs={'placeholder': 'Додайте відповідь'})}

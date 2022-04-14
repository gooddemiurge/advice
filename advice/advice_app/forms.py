from .models import Post
from django.forms import ModelForm, Textarea

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "question", "isClosed"]
        widgets = {"question": Textarea(attrs={'placeholder': 'Введіть назву'})}

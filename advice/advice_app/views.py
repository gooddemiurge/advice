from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Answer
from .forms import PostForm, AnswerForm
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import ListView, DetailView, CreateView


# Create your views here.

class Main_page(ListView):
    model = Post
    queryset = Post.objects.order_by('-id')[:10]
    template_name = "advice_app/index.html"


class Post_detail(DetailView):
    model = Post
    template_name = "advice_app/detail.html"

# class Add_answer(CreateView):
#     form_class = AnswerForm
#     template_name = "advice_app/detail.html"
#     context_object_name = "answer"


def add_post(request):
    error = ''
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('index')
        else:
            error = 'Недійсна форма'

    form = PostForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'advice_app/add_post.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'advice_app/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')
    form = AuthenticationForm()
    return render(request, 'advice_app/login.html', {'form': form})




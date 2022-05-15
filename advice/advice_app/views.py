from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import FormMixin

from .models import Post, Answer
from .forms import PostForm, AnswerForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import ListView, DetailView


# Create your views here.

class Main_page(ListView):
    model = Post
    queryset = Post.objects.order_by('-id')[:10]
    template_name = "advice_app/index.html"

class My_posts(ListView):
    Model = Post
    template_name = "advice_app/my_posts.html"

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

def delete_post(request, pk=None):
    post_to_delete = Post.objects.get(id=pk)
    post_to_delete.delete()
    return HttpResponseRedirect(reverse('index'))

def delete_answer(request, pk=None):
    page = request.META.get('HTTP_REFERER')
    answer_to_delete = Answer.objects.get(id=pk)
    answer_to_delete.delete()
    return redirect(page)

class Post_detail(FormMixin, DetailView):
    model = Post
    template_name = "advice_app/detail.html"
    form_class = AnswerForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('detail', kwargs={'pk':self.get_object().id})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        page = request.META.get('HTTP_REFERER')
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return redirect(page)




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




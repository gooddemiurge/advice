from django.contrib import messages, auth
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import FormMixin, UpdateView
from .models import Post, Answer, KeyWords
from .forms import PostForm, AnswerForm, SignUpForm, LoginForm
from django.contrib.auth import login as auth_login, authenticate
from django.views.generic import ListView, DetailView


class MainPage(ListView):
    model = Post
    queryset = Post.objects.order_by('-id')
    template_name = "advice_app/index.html"


class Search(ListView):
    model = Post
    template_name = 'advice_app/search.html'

    def get_queryset(self):
        search_query = self.request.GET.get('search', '')
        search_list = search_query.split()
        search_result = []

        for keyword_user_wants in search_list:
            if KeyWords.is_key_word(keyword_user_wants):
                dbContainsKeyword = KeyWords.objects.filter(word=keyword_user_wants).exists()
                if not dbContainsKeyword:
                    new_word = KeyWords(word=keyword_user_wants)
                    new_word.save()
                else:
                    new_word = KeyWords.objects.get(word=keyword_user_wants)

                relevantPosts = Post.objects.filter(Q(title__icontains=keyword_user_wants) | Q(question__icontains=keyword_user_wants))
                if not relevantPosts:
                    relevantPosts = Post.objects.filter(Q(title__icontains=KeyWords.translate(keyword_user_wants)) | Q(question__icontains=KeyWords.translate(keyword_user_wants)))

                for post in relevantPosts:
                    new_word.posts.add(post.id)
                    if post not in search_result:
                        search_result.append(post)

        return search_result


class MyPosts(ListView):
    Model = Post
    template_name = "advice_app/my_posts.html"

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-id')


def delete_post(request, pk=None):
    post_to_delete = Post.objects.get(id=pk)
    post_to_delete.delete()
    return HttpResponseRedirect(reverse('index'))


def delete_answer(request, pk=None):
    page = request.META.get('HTTP_REFERER')
    answer_to_delete = Answer.objects.get(id=pk)
    answer_to_delete.delete()
    return redirect(page)


def change_status(request, pk=None):
    page = request.META.get('HTTP_REFERER')
    post = Post.objects.get(id=pk)
    post.isClosed = not post.isClosed
    post.save()
    return redirect(page)


class PostDetail(FormMixin, DetailView):
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


class EditPost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'advice_app/edit.html'


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
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'advice_app/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')
    form = LoginForm()
    return render(request, 'advice_app/login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('index')




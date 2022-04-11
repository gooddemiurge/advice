from django.shortcuts import render, redirect
from .models import Post, Answer
from .forms import PostForm

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-id')
    return render(request, 'advice_app/index.html', {'posts': posts})

def about_us(request):
    return render(request, 'advice_app/about.html')

def add_post(request):
    error = ''
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Недійсна форма'

    form = PostForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'advice_app/add_post.html', context)





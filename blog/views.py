from django.shortcuts import render, redirect
from .models import Post
from .form import PostForm
from django.utils import timezone
from django.http import Http404
from django.http import HttpResponse

# Create your views here.
def create(request):
    if request.method=='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = PostForm()

    return render(request, 'major/form.html', {'form': form})

def go_home(request):
    return render(request, 'major/base.html')

def item_menu1(request):
    return render(request, 'major/item_menu1.html')

def item_menu2(request):
    return render(request, 'major/item_menu2.html')

def item_menu3(request):
    return render(request, 'major/item_menu3.html')


def index(request):
    try:
        list = Post.objects.order_by('-pub_date')[:]
    except Post.DoesNotExist:
        raise Http404("Post Not Found")

    context = {'list': list}
    return render(request, 'major/index.html', context)



from blog.models import Blog
from django.shortcuts import get_object_or_404, render
from django.db.models import Q


def index(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/index.html', {'blogs': blogs})


def blog_details(request, slug, id=None):
    instance = get_object_or_404(Blog, id=id)
    blog = {'instance': instance}
    return render(request, 'blog/blog_details.html', blog)


def django_index(request):
    django = Blog.objects.filter(Q(category__title__contains ='django'))
    return render(request, 'django/index.html', {'django': django })


def python_index(request):
    python = Blog.objects.filter(Q(category__title__contains ='python'))
    return render(request, 'python/index.html', {'python': python })


def linux_index(request):
    linux = Blog.objects.filter(Q(category__title__contains ='linux'))
    return render(request, 'linux/index.html', {'linux': linux })


def windows_index(request):
    windows = Blog.objects.filter(Q(category__title__contains ='windows'))
    return render(request, 'python/index.html', {'windows': windows })

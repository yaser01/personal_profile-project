from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('-score')
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
    try:
        blog = get_object_or_404(Blog, pk=blog_id)
        return render(request, 'blog/detail.html', {'blog': blog})
    except Http404:
        print("HRLL")
        return render(request, 'blog/404.html')

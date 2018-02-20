from django.shortcuts import render
from blog.models import *


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)
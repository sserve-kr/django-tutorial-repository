from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def post_view(request, post_id):
    post_obj = get_object_or_404(Post, pk=post_id)
    return render(request, 'post/view.html', {'post': post_obj})

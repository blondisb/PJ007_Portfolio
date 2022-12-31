from django.shortcuts import render, get_object_or_404
from .models import MO_blogs

# Create your views here.
def VW_posts(request):
    posts = MO_blogs.objects.all()
    return render(request, 'posts.html', {
        'posts': posts
    })

def VW_post_detail(request, pk):
    # post = MO_blogs.objects.get(id=request.GET.get('id'))
    # post = MO_blogs.objects.get(id=pk)
    post = get_object_or_404(MO_blogs, pk=pk)
    return render(request, 'post_detail.html', {
        'post': post
    })


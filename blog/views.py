from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils import timezone
from .foms import BlogPostForm, CommentForm
from .models import BlogPost

def index(request):
    post_list = BlogPost.objects.order_by('-created_date')
    context = {'post_list': post_list}
    return render(request, 'blog/blog_post_list.html', context)

def view_post(request, post_id):
    blog_post = get_object_or_404(BlogPost, pk=post_id)
    context = {'blog_post': blog_post}
    return render(request, 'blog/blog_post_view.html', context)

def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post_form = form.save(commit=False)
            post_form.created_date = timezone.now()
            post_form.save()
            return redirect('blog:blog_home')
    else:
        form = BlogPostForm()
        context = {'form': form}
        return render(request, 'blog/create_post.html', context)

def submit_comment(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_form = form.save(commit=False)
            comment_form.created_date = timezone.now()
            comment_form.blog_post = post
            comment_form.save()
            return redirect('blog:view_post', post_id=post_id)
        else:
            return HttpResponse('That something wrong')
    else:
        return HttpResponse('Only POST Method Can Access')
    context = {'post': post}
    return render(request, 'blog/blog_post_view.html', context)




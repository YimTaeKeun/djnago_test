from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .models import Question
from .forms import PostForm

def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

def write_post(request):
    if request.method == 'POST':
        post = PostForm(request.POST)
        if post.is_valid():
            question = post.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:home')
    else:
        post = PostForm()
    context = {'post': post}
    return render(request, 'pybo/write_post_view.html', context)

def view_post(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/post_detail.html', context)





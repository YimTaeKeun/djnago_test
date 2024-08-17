from django import forms
from .models import Question

class PostForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'subject']
        labels = {'question': '제목', 'subject': '내용'}

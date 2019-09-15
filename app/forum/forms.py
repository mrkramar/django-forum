from django import forms

from .models import Comment

class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'body', 'author', 'post'
        ]
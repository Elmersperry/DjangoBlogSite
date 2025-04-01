from django import forms
from django.contrib.auth.models import User

class PostForm(forms.Form):
    author = forms.ModelChoiceField(queryset=User.objects.all(), label="Автор")
    title = forms.CharField(max_length=200, label="Заголовок")
    text = forms.CharField(widget=forms.Textarea, label="Текст поста")
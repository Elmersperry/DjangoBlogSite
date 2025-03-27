from django import forms
from django.contrib.auth.models import User

class PostForm(forms.Form):
    author = forms.ModelChoiceField(queryset=User.objects.all())
    title = forms.CharField(max_length=200)
    text = forms.TextInput()
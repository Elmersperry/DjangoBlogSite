from django import forms
from django.contrib.auth.models import User
from .models import Post

# class PostForm(forms.Form):
#     title = forms.CharField(max_length=200, label="Заголовок")
#     text = forms.CharField(widget=forms.Textarea, label="Текст поста")
#     author = forms.ModelChoiceField(queryset=User.objects.all(), label="Автор")
#     image = forms.ImageField(required=False, label="Изображение")

class PostForm(forms.ModelForm):
    # Дополняем конструктор родительского класса
    def __init__(self, *args, **kwargs):
        # получаем author из именованных вргументов (его передали во views)
        author = kwargs.pop('author', None)
        # вызывем конгструктор родительского класса
        super(PostForm, self).__init__(*args, **kwargs)
        # устанавливаем начальное значение поля author
        self.fields['author'].initial = author
        # отключаем видимость этого поля в форме
        self.fields['author'].disabled = True
        self.fields['author'].widget = forms.HiddenInput()

    class Meta:
        model = Post
        fields = ('author','title', 'text', 'image')

        labels = {
            'title': 'Заголовок',
            'text': 'Текст поста',
            'image': 'Изображение'
        }

class FilterForm(forms.Form):
    author = forms.ModelChoiceField(queryset=User.objects.all(), label='Автор', required=False)
    created_at = forms.DateField(label='Дата публикации',
                                 widget=forms.DateInput(attrs={'type': 'date'}),
                                 input_formats=['%Y-%m-%d'],
                                 required=False)

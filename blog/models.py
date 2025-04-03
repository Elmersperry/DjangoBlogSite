from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# описание модели поста
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст поста")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания", editable=False)
    image = models.ImageField(upload_to='posts/', null=True, verbose_name="Изображение")

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title
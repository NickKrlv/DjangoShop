from django.db import models
from django.utils.text import slugify

NULLABLE = {'blank': True, 'null': True}


class BlogPost(models.Model):
    title = models.CharField(max_length=300, verbose_name='title')
    slug = models.CharField(max_length=300, **NULLABLE, verbose_name='slug')
    content = models.TextField(verbose_name='content')
    preview = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='preview')
    date_created = models.DateField(auto_now_add=True, verbose_name='date_created')
    view_count = models.IntegerField(default=0, verbose_name='view_count')
    is_published = models.BooleanField(default=True, verbose_name='is_published')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'

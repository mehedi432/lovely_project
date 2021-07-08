from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=21)

    class Meta:
        verbose_name_plural='categories'

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.TextField(unique=True, max_length=987)
    updated = models.DateField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = HTMLField()
    slug = models.SlugField(blank=True, max_length=987)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("details", kwargs={"id": self.id, 'slug': self.slug})
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


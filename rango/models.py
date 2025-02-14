from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=128, null=False, default="Unnamed")  
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(blank=True, unique=True)  

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name  

    def save(self, *args, **kwargs):
        if not self.slug and self.name:  
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Page(models.Model):
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
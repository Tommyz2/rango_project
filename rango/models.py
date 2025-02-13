from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=128, null=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(blank=True, default="")  # ✅ 让 slug 默认值为空字符串

    class Meta:
         verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name  

    def save(self, *args, **kwargs):
        if not self.slug and self.name:  # ✅ 防止 name 为空时报错
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)  # 正确的 super() 调用


class Page(models.Model):
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):  # ✅ 修复缩进问题
        return self.user.username
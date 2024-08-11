from django.utils import timezone
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


class CategoryModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Kategoriya nomi')
    slug = models.SlugField(max_length=300)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("category_detail_page", args=[self.slug])

    class Meta:
        db_table = 'Categorys'
        managed = True
        verbose_name = 'Kategoriyalar'
        verbose_name_plural = 'Kategoriyalar'
        
        
class ActivedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='Faol')
    
    
class NewsModel(models.Model):
    
    class Status(models.TextChoices):
        Deactive = 'Faol emas', 'Faol emas'
        Active  = 'Faol', 'Faol'
        
    title = models.CharField(max_length=250, verbose_name='Yangilik nomi')
    slug = models.SlugField(max_length=250)
    body = models.TextField(verbose_name="Yangilik haqida ma'lumotlar")
    image = models.ImageField(upload_to='news/images', verbose_name='Rasmi')
    category = models.ForeignKey(CategoryModel, 
                                 on_delete=models.CASCADE,
                                 verbose_name='Kategoriyasi'
                                 )
    publish_time = models.DateTimeField(default=timezone.now, verbose_name='Yangilik yaratilgan vaqt')
    created_time = models.DateTimeField(auto_now_add=True)
    updeted_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, 
                              choices=Status.choices, 
                              default=Status.Deactive,
                              verbose_name='Holati'
                              )
    view_count = models.IntegerField(default=0)
    objects = models.Manager()
    manager = ActivedManager()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("news_detail_page", args=[self.slug])
    
    class Meta:
        ordering = ['-publish_time']
        db_table = 'News'
        managed = True
        verbose_name = 'Yangiliklar'
        verbose_name_plural = 'Yangiliklar'


class CommentModel(models.Model):
    news = models.ForeignKey(NewsModel,
                             on_delete=models.CASCADE,
                             related_name='comments')
    user = models.ForeignKey(User, 
                             on_delete=models.CASCADE,
                             related_name='comments')
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_time']
        db_table = 'Comments'
        managed = True
        verbose_name = 'Izoh'
        verbose_name_plural = 'Izohlar'

    def __str__(self):
        return f"Comment = {self.body} by {self.user}"
        
    
class ContactModel(models.Model):
    
    name = models.CharField(max_length=50, verbose_name='Ism')
    email = models.EmailField(max_length=254, verbose_name='Email')
    message = models.TextField(verbose_name='Xabar')
    
    def __str__(self) -> str:
        return self.email

    class Meta:
        db_table = 'Contact'
        managed = True
        verbose_name = 'Aloqa'
        verbose_name_plural = 'Aloqa'
    
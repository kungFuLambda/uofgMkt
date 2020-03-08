from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User





# Create your models here.
class Listing(models.Model):
    picture = models.ImageField(default=0)
    #seller = models.ForeignKey('User',on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    price = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name


class UserProfile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=128,unique=True)
    slug = models.SlugField()
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Category,self).save(*args,**kwargs)



    class Meta: 
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
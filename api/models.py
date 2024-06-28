from django.db import models
from django.utils import timezone
class Products(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

class NewsLetter(models.Model):
    email = models.CharField(max_length=140)
    
    def __str__(self):
        return self.email
    
class NewProducts(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    image = models.ImageField(upload_to='new_products/')

    def __str__(self):
        return self.name
    

class OurGallery(models.Model):
    image = models.ImageField(upload_to='our_gallery')


class ShortCattegorys(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=120,blank=True,null=True)
    

    def __str__(self):
        return self.name
    
class LastBlogs(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='blogs_image/')
    created_at = models.DateField(auto_now_add=True)
    chislo = models.CharField(max_length=10, blank=True)
    oy = models.CharField(max_length=10, blank=True)
    def save(self, *args, **kwargs):
        if not self.pk:  # faqat yangi ob'ekt yaratishda
            self.created_at = timezone.now().date()  # vaqtni olish
            self.chislo = self.created_at.strftime("%d")
            self.oy = self.created_at.strftime("%b")
        super(LastBlogs, self).save(*args, **kwargs)

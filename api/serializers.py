from rest_framework import serializers
from .models import Products,NewsLetter,NewProducts,OurGallery,ShortCattegorys,LastBlogs

class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id','name','price','image')


class NewsLetterSerializers(serializers.ModelSerializer):
    class Meta:
        model = NewsLetter
        fields = ('id','email')

class NewsProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = NewProducts
        fields = ('id','name','price','image')

class OurGallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = OurGallery
        fields = ('id','image')

class ShortCattegorysSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShortCattegorys
        fields = ('id','name','url')

class LastBlogsSerializers(serializers.ModelSerializer):
    class Meta:
        model = LastBlogs
        fields = ('id','name','image','chislo','oy')
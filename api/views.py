from rest_framework import generics
from .models import Products,NewsLetter,NewProducts,OurGallery,ShortCattegorys,LastBlogs
from .serializers import ProductsSerializers,NewsLetterSerializers,NewsProductsSerializers,OurGallerySerializers,ShortCattegorysSerializers,LastBlogsSerializers


class ProductsListCreateView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers

class NewsLetterListCreateView(generics.ListCreateAPIView):
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterSerializers

class NewProductsListCreateView(generics.ListCreateAPIView):
    queryset = NewProducts.objects.all()
    serializer_class = NewsProductsSerializers

class OurGalleryListCreateView(generics.ListCreateAPIView):
    queryset = OurGallery.objects.all()
    serializer_class = OurGallerySerializers

class ShortCattegorysListCreateView(generics.ListCreateAPIView):
    queryset = ShortCattegorys.objects.all()
    serializer_class = ShortCattegorysSerializers

class LastBlogsListCreateView(generics.ListCreateAPIView):
    queryset = LastBlogs.objects.all()
    serializer_class = LastBlogsSerializers
# urls.py
from django.urls import path
from .views import ProductsListCreateView,NewsLetterListCreateView, \
NewProductsListCreateView,OurGalleryListCreateView,ShortCattegorysListCreateView,\
LastBlogsListCreateView
urlpatterns = [
    path('api/products/', ProductsListCreateView.as_view(), name='products-list-create'),
    path('api/newsletter/', NewsLetterListCreateView.as_view(), name='newsletter-list-create'),
    path('api/newproducts/',NewProductsListCreateView.as_view(),name='newproducts-list-create'),
    path('api/ourgallery/',OurGalleryListCreateView.as_view(),name='ourgallery-list-create'),
    path('api/shortcattegorys/',ShortCattegorysListCreateView.as_view(),name='shortcattegorys-list-create'),
    path('api/lastblogs/',LastBlogsListCreateView.as_view(),name='lastblogs-list-create')
]
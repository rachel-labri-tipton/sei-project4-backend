from django.shortcuts import render
from rest_framework import generics
from blog_categories.models import Category
from blog_categories.serializers import CategoryEditorSerializer, CategorySerializer

# Create your views here.


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryEditorSerializer

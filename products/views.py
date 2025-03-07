from django.shortcuts import render,redirect,get_object_or_404
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from .forms import ProductForm
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def product_list(request):
    products=Product.objects.all()
    return render(request,'list.html',{'products':products})

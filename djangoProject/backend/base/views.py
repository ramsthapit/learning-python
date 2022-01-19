from itertools import product
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serilizers import ProductSerializer

from .models import Product

# Create your views here.


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serilizer = ProductSerializer(products, many=True)
    return Response(serilizer.data)


@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serilizer = ProductSerializer(product, many=False)
    return Response(serilizer.data)

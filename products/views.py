from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def home(request):
    categories = Category.objects.all()
    products = Product.objects.filter(
        featured=True,
        available=True
    )

    return render(request, "home.html", {
        "categories": categories,
        "products": products,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    return render(request, "product_detail.html", {
        "product": product
    })
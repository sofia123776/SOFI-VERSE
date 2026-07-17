from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from reviews.models import Review
from reviews.forms import ReviewForm
from django.db.models import Avg


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

    reviews = Review.objects.filter(
        product=product
    ).order_by('-created_at')

    form = ReviewForm()

    average_rating = reviews.aggregate(
        Avg('rating')
    )['rating__avg']

    return render(request, "products/product_detail.html", {
        "product": product,
        "reviews": reviews,
        "form": form,
        "average_rating": average_rating,
    })
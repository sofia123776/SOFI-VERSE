from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from reviews.models import Review
from reviews.forms import ReviewForm
from django.db.models import Avg
from django.core.paginator import Paginator
from django.db.models import Q


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

def shop(request):

    products = Product.objects.filter(available=True)
    categories = Category.objects.all()

    search = request.GET.get("search")
    category = request.GET.get("category")
    sort = request.GET.get("sort")

    if search:
        products = products.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search)
        )

    if category:
        products = products.filter(category__id=category)

    if sort == "low":
        products = products.order_by("price")

    elif sort == "high":
        products = products.order_by("-price")

    elif sort == "name":
        products = products.order_by("name")

    else:
        products = products.order_by("-id")

    paginator = Paginator(products, 8)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(request, "products/shop.html", {
        "page_obj": page_obj,
        "categories": categories,
    })
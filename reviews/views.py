from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Review
from .forms import ReviewForm


@login_required
def add_review(request, slug):

    product = get_object_or_404(Product, slug=slug)

    review = Review.objects.filter(
        product=product,
        user=request.user
    ).first()

    if request.method == "POST":

        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()

    return redirect('product_detail', slug=slug)
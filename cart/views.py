from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from products.models import Product
from .models import CartItem


@login_required
def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


@login_required
def cart(request):

    cart_items = CartItem.objects.filter(
        user=request.user
    )

    total = sum(item.total_price for item in cart_items)

    return render(
        request,
        'cart/cart.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )



def increase_quantity(request, item_id):

    item = get_object_or_404(CartItem, id=item_id, user=request.user)

    item.quantity += 1
    item.save()

    return redirect("cart")


def decrease_quantity(request, item_id):

    item = get_object_or_404(CartItem, id=item_id, user=request.user)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect("cart")


def remove_item(request, item_id):

    item = get_object_or_404(CartItem, id=item_id, user=request.user)

    item.delete()

    return redirect("cart")
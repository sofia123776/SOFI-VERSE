from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from cart.models import CartItem
from .models import Order, OrderItem
from .forms import CheckoutForm


@login_required
def checkout(request):

    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items.exists():
        return redirect("cart")

    total = sum(item.total_price for item in cart_items)

    if request.method == "POST":

        form = CheckoutForm(request.POST)

        if form.is_valid():

            order = form.save(commit=False)

            order.user = request.user
            order.total = total
            order.save()

            for item in cart_items:

                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )

            cart_items.delete()

            return redirect("order_success", order.id)

    else:

        form = CheckoutForm()

    return render(request, "orders/checkout.html", {
        "form": form,
        "cart_items": cart_items,
        "total": total
    })


@login_required
def order_success(request, order_id):

    order = Order.objects.get(id=order_id)

    return render(request, "orders/order_success.html", {
        "order": order
    })


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'orders/my_orders.html', {
        'orders': orders
    })
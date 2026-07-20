from django.shortcuts import render


def about(request):
    return render(request, "core/about.html")


def contact(request):
    return render(request, "core/contact.html")


def faq(request):
    return render(request, "core/faq.html")


def privacy(request):
    return render(request, "core/privacy.html")


def terms(request):
    return render(request, "core/terms.html")
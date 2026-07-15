from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")

    else:
        form = UserCreationForm()

    for field in form.fields.values():
        field.widget.attrs.update({
            'class': 'form-control',
            'placeholder': field.label
        })

    return render(request, "accounts/register.html", {
        "form": form
    })

def user_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'accounts/login.html')


def user_logout(request):
    logout(request)
    return redirect('home')


def profile(request):
    return render(request, 'accounts/profile.html')
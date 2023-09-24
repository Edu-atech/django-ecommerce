from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("frontend:item-list")
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        signin_form = AuthenticationForm(data=request.POST)
        if signin_form.is_valid():
            user = signin_form.get_user()
            login(request, user)

            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("frontend:item-list")
    else:
        signin_form = AuthenticationForm()

    return render(request, "login.html", {"signin_form": signin_form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
    return redirect("frontend:item-list")

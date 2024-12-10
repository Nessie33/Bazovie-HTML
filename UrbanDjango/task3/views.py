from django.shortcuts import render


def one(request):
    return render(request, "platform.html")


def two(request):
    return render(request, "games.html")


def three(request):
    return render(request, "cart.html")
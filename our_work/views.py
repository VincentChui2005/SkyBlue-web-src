from django.shortcuts import render


def home(request):
    return render(request, "our_work/home.html")

from django.shortcuts import render
from django.http import FileResponse


def home(request):
    return render(request, 'home.html')


def about_us(request):
    return render(request, 'about_us.html')


def our_client(request):
    return render(request, 'our_client.html')


def link(request):
    return render(request, 'link.html')


def contact_us(request):
    return render(request, 'contact_us.html')


def join_us(request):
    return render(request, 'join_us.html')

def load_static(request, filepath):
    return FileResponse(open(f"static/{filepath}", "rb"))

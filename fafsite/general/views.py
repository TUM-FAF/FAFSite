from django.shortcuts import render


def index(request):
    return render(request, "mainpage.html", {"activepage": "index"})


def about(request):
    return render(request, "about.html", {"activepage": "About"})


def admission(request):
    return render(request, "admission.html", {"activepage": "Admission"})


def thankyou(request):
    return render(request, "credits.txt", content_type='text/plain')

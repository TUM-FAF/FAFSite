from django.shortcuts import render


def authenticate(request):
    return render(request, 'auth.html', {})

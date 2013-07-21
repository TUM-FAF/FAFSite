from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from academics.models import User
from .forms import Profile


# @login_required(login_url='/login/')
def fafside_index(request):
    return render(request, 'fafside/main.html')


@login_required(login_url='/login/')
def profile(request):
    email = request.user.email
    try:
        user = User.objects.get(email=email)
        param_dict = {"user": user}
    except DoesNotExist:
        param_dict = {}
    form = Profile()
    return render(request, 'fafside/profile.html', param_dict)

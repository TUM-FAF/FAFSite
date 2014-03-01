from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from general.models import FAFUser
from .forms import Profile


# @login_required(login_url='/login/')
def fafside_index(request):
    return render(request, 'fafside/main.html')


# @login_required
def profile(request):
    # email = request.user.email
    email = "ana.balica@gmail.com"
    try:
        user = FAFUser.objects.get(email=email)
        param_dict = {"user": user}
    except DoesNotExist:
        param_dict = {}
    form = Profile()
    # add_placeholders(form, user)

    param_dict["form"] = form
    return render(request, 'fafside/profile.html', param_dict)


def add_placeholders(form, user):
    pass

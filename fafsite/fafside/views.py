from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from academics.models import UserExtended, User
from .forms import Profile


@login_required(login_url='/login/')
def fafside_index(request):
    return render(request, 'fafside/main.html')


@login_required(login_url='/login/')
def profile(request):
    email = request.user.email
    user = User.objects.get(email=email)
    user_extended = UserExtended(user.id)
    form = Profile()
    for field in form.fields:
        form.fields.get(field).initial = getattr(user_extended, field)
    return render(request, 'fafside/profile.html', {"form": form})

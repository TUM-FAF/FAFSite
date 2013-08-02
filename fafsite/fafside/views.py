from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from academics.models import UserExtended, User
from .forms import Profile


@login_required(login_url='/login/')
def fafside_index(request):
    return render(request, 'fafside/main.html')


@csrf_exempt
@login_required(login_url='/login/')
def profile(request):
    email = request.user.email
    user = User.objects.get(email=email)
    user_extended = UserExtended(user.id)
    form = Profile()
    if request.method == 'POST':
        form = Profile(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            for field in cd:
                setattr(user_extended, field, cd.get(field))
    else:
        for field in form.fields:
            form.fields.get(field).initial = getattr(user_extended, field)
    return render(request, 'fafside/profile.html', {"form": form})

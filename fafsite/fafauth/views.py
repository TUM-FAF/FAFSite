from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth.views import password_reset, password_reset_confirm
from .controllers import ExtendedUserCreationForm, ExtendedAuthenticationForm
from django.core.urlresolvers import reverse
from django.conf import settings


def login_view(request):
  if request.user.is_authenticated():
    return loggedin(request)

  nextpage = request.GET.get('next', reverse('faflabs_dashboard'))

  if request.method != 'POST':
    form = ExtendedAuthenticationForm()
  else:
    form = ExtendedAuthenticationForm(data=request.POST)
    if form.is_valid():
      login(request, form.get_user())
      return HttpResponseRedirect(nextpage)

  return render(request, 'fafauth/login.html', {
      "form": form
    , "activepage": "Login"
    })

def loggedin(request):
  return render(request, 'fafauth/loggedin.html', {})

def logout_view(request):
  logout(request)
  return render(request, 'fafauth/logout.html', {})

def register_view(request):
  logout(request)

  if request.method != 'POST':
    form = ExtendedUserCreationForm()
  else:
    form = ExtendedUserCreationForm(data=request.POST)
    if form.is_valid():
      nextpage = request.GET.get('next', reverse('faflabs_dashboard'))

      username = form.clean_username()
      password = form.clean_password2()
      # form save should be after clean_username as otherwise it will rise 'username exists' error
      user = form.save()

      # authenticate before login
      user = authenticate(username=username, password=password)
      login(request, user)

      return HttpResponseRedirect(nextpage)

  return render(request, 'fafauth/register.html', {
      "form": form
    , "activepage": "Register"
    })

def passwordreset_view(request):
  return password_reset(request, email_template_name='fafauth/passwordreset_email.html',
    template_name='fafauth/passwordreset.html', post_reset_redirect=reverse('passwordreset_initiated'))

  form = PasswordResetForm(None, request.POST)

  if request.method == 'POST':
    if form.is_valid():
      form.save(from_email=settings.EMAIL_HOST_USER, email_template_name='fafauth/passwordreset_email.html')

  return render(request, 'fafauth/passwordreset.html', {
      "form": form
    , "activepage": "Password Reset"
    })

def passwordreset_confirm(request, uidb64=None, token=None):
  # Wrap the built-in reset confirmation view and pass to it all the captured parameters like uidb64, token
  # and template name, url to redirect after password reset is confirmed.
  return password_reset_confirm(request, template_name='fafauth/passwordreset_confirm.html',
    uidb64=uidb64, token=token, post_reset_redirect=reverse('passwordreset_success'))

def passwordreset_initiated(request):
  return render(request, 'fafauth/passwordreset_initiated.html')

def passwordreset_success(request):
  return render(request, 'fafauth/passwordreset_success.html')

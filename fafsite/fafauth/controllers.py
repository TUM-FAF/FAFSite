import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from academics.helpers import link_auth_user
from academics.models import GROUPS

"""
Based on
https://gist.github.com/fohlin/771052
"""

class UniqueUserEmailField(forms.EmailField):
  """
  An EmailField which only is valid if no User has that email.
  """
  def validate(self, value):
    super(forms.EmailField, self).validate(value)
    try:
      User.objects.get(email = value)
      raise forms.ValidationError("Email already exists")
    except User.MultipleObjectsReturned:
      raise forms.ValidationError("Email already exists")
    except User.DoesNotExist:
      pass

class ExtendedUserCreationForm(UserCreationForm):
  """
  Extends the built in UserCreationForm in several ways:

  * Adds an email field, which uses the custom UniqueUserEmailField,
    that is, the form does not validate if the email address already exists
    in the User table.
  * The username field is generated based on the email, and isn't visible.
  * Data not saved by the default behavior of UserCreationForm is saved.
  """

  username = forms.CharField(required = False, max_length = 30)
  email = UniqueUserEmailField(required = True, label = 'Email address')
  name = forms.CharField(required=True, max_length=127)
  surname = forms.CharField(required=True, max_length=127)
  group = forms.ChoiceField(required=True, choices=GROUPS)

  def __init__(self, *args, **kwargs):
    """
    Changes the order of fields, and removes the username field.
    """
    super(UserCreationForm, self).__init__(*args, **kwargs)
    self.fields.keyOrder = ['email', 'password1', 'password2', 'name', 'surname', 'group']

  def clean(self, *args, **kwargs):
    """
    Normal cleanup + username generation.
    """
    cleaned_data = super(UserCreationForm, self).clean(*args, **kwargs)
    if cleaned_data.has_key('email'):
      cleaned_data['username'] = cleaned_data['email']
    return cleaned_data

  def save(self, commit=True):
    """
    Saves the email after the normal save behavior is complete.
    Create academics user if everything is successful
    """
    user = super(UserCreationForm, self).save(commit)
    if user:
      user.email = self.cleaned_data['email']
      user.set_password(self.cleaned_data['password1'])
      if commit:
        user.save()
        link_auth_user(user, self.cleaned_data)
    return user

class ExtendedAuthenticationForm(AuthenticationForm):
  username = forms.CharField(required = True, label = 'Email')

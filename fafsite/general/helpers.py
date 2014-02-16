from .models import FAFUser, UserExtended

def link_auth_user(auth_user, data):
  # search for academics user with the same Name, Surname and Group
  faf_user = FAFUser.objects.filter(auth_user=None, first_name=data['first_name'], last_name=data['last_name'], group=data['group'])

  if not faf_user:
    # if not found - create a new faf user
    faf_user = FAFUser(first_name=data['first_name'], last_name=data['last_name'], group=data['group'], auth_user=auth_user)
    faf_user.save()

  else:
    # extract first match from Query set
    faf_user = faf_user[0]

  faf_user.auth_user = auth_user
  faf_user.save()

def get_faf_user_by_auth_user(auth_user):
  user = FAFUser.objects.get(auth_user=auth_user)
  user_extended = UserExtended(user.id)

  return user_extended

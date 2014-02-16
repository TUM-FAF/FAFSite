from .models import FAFUser, UserExtended

def link_auth_user(auth_user, data):
  # search for academics user with the same Name, Surname and Group
  user = FAFUser.objects.filter(auth_user_id=0, name=data['name'], surname=data['surname'], group=data['group'])

  if not user:
    # search for academics user with the same email
    user = FAFUser.objects.filter(auth_user_id=0, email=data['email'])

    if not user:
      # if not found - create a new academics user
      user = FAFUser(name=data['name'], surname=data['surname'], group=data['group'], auth_user_id=auth_user.id, email=data['email'])
      user.save()

    else:
      # extract first match from Query set
      user = user[0]
  else:
    # extract first match from Query set
    user = user[0]

  user.auth_user_id = auth_user.id
  user.save()

def get_academics_user_by_auth_user_id(id):
  user = FAFUser.objects.get(auth_user_id=id)
  user_extended = UserExtended(user.id)

  return user_extended

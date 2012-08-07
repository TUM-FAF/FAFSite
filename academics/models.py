from django.db import models

KEYS = (
	('USER_TYPE', 'User type'),
	('PHOTO', 'Photo'),
	('CURRENT_JOB', 'Current job'),
	)

TYPES = (
	('CharField(max_length=63)', 'Char Field'),
	('TextField()', 'Text Field'),
	)

class User(models.Model):
	name = models.CharField(max_length=15)
	surname = models.CharField(max_length=31)
	email = models.EmailField()
	group = models.CharField(blank=True, max_length=15)

	def __unicode__(self):
		return u'%s %s' % (self.name, self.surname)

class UserMetaType(models.Model):
	key = models.TextField()
	type = models.TextField()
	data = models.TextField(blank=True)
	multiple = models.BooleanField()

	def __unicode__(self):
		return u'%s' % (self.key)

class UserMeta(models.Model):
	user = models.ForeignKey(User)
	meta = models.ForeignKey(UserMetaType)
	value = models.TextField()

	def __unicode__(self):
		return u'%s - %s' % (self.meta, self.value)

'''
====Proxy Object for User class and it's attributes====

=	Load user 				user = UserExtended(user_id)

=	Load empty user 		user = UserExtended()

=	Get user attributes		user.age
	returns:				string (if not multiple meta)
							array of strings (if multiple meta)

=	Chech if some attribute user.hasattr('type')
	is defined

=	Update user attributes	user.age = 25
							user.type = ['student', 'mentor'] (if multiple meta)

=	Delete user attributes	del user.age

=	Delete user and all		del user
	its meta
'''
class UserExtended():
	def __init__(self, user_id=0):
		if user_id <= 0:
			self.user = User()
		else:
			try:
				self.user = User.objects.get(id=user_id)
			except User.DoesNotExist:
				self.user = User()

	def __setattr__(self, key, value):
		if key == "user":
			self.__dict__[key] = value
		elif hasattr(self.user, key):
			setattr(self.user, key, value)
			salf.user.save()
		else:
			return self.setMeta(key, value)

	def __getattr__(self, key):
		if hasattr(self.user, key):
			return getattr(self.user, key)
		else:
			return self.getMeta(key)

	def __delattr__(self, key):
		if key == "user":
			del self.__dict__[key]
		else:
			self.delMeta(key)

	def __del__(self):
		self.user.delete()
		# delete all attributes
		UserMeta.objects.filter(user=self.user).delete()

	def hasattr(self, key):
		if hasattr(self.user, key):
			return True
		else:
			try:
				getattr(self, key)
				return True
			except:
				return False

	#TODO: check for meta_type filters
	def setMeta(self, key, value):
		try:
			meta_type = UserMetaType.objects.get(key=key)
		except UserMetaType.DoesNotExist:
			raise AttributeError("such meta key not defined")
		except:
			raise AttributeError("unknown error")

		if meta_type.multiple:
			delattr(self, key)	# delete all meta of this type
			if type(value) == type([]) or type(value) == type(list()):
				for value_one in value:
					self.addMeta(key, value_one)
			else:
				self.addMeta(key, value)
		else:
			try:
				user_meta = UserMeta.objects.get(user=self.user, meta=meta_type)
			except UserMeta.DoesNotExist:
				user_meta = UserMeta(user=self.user, meta=meta_type)	# new meta
			except:
				raise AttributeError("unknown error")
				
			user_meta.value = value
			user_meta.save()		
		
	def addMeta(self, key, value):
		try:
			meta_type = UserMetaType.objects.get(key=key)
		except UserMetaType.DoesNotExist:
			raise AttributeError("such meta key not defined")
		except:
			raise AttributeError("unknown error")

		user_meta = UserMeta(user=self.user, meta=meta_type, value=value)
		user_meta.save()

	def getMeta(self, key):
		try:
			meta_type = UserMetaType.objects.get(key=key)
		except UserMetaType.DoesNotExist:
			raise AttributeError("no such meta type")
		except:
			raise AttributeError("unknown error")

		try:
			if not meta_type.multiple:
				meta = UserMeta.objects.get(user=self.user, meta=meta_type)
				return meta.value
			else:
				# return array of values
				result = []
				for meta in UserMeta.objects.filter(user=self.user, meta=meta_type):
					result.append(meta.value)
				return result

		except UserMeta.DoesNotExist:
			raise AttributeError("no such meta")
		except UserMeta.MultipleObjectsReturned:
			raise AttributeError("multiple objects returned")
		except:
			raise AttributeError("unknown error")
		
		raise AttributeError()

	def delMeta(self, key):
		try:
			meta_type = UserMetaType.objects.get(key=key)
			try:
				return UserMeta.objects.filter(user=self.user, meta=meta_type).delete()
			except:
				return False
		except:
			return False

	

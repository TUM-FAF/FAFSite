from django.db import models

# RANKINGS = (
# 	('LECT', 'Lecturer'),
# 	('LECT_SUP', 'Superior lecturer'),
# 	('PHD', 'PhD'),
# 	('SEN_LECT', 'Senior Lecturer'),

# 	)

# SEMESTERS = (
# 	(1, 'I'),
# 	(2, 'II'),
# 	(3, 'III'),
# 	(4, 'IV'),
# 	(5, 'V'),
# 	(6, 'VI'),
# 	(7, 'VII'),
# 	)

# LANGUAGES = (
# 	('EN', 'English'),
# 	('RO', 'Romanian'),
# 	)

# class Student(models.Model):
# 	name = models.CharField(max_length=15)
# 	surname = models.CharField(max_length=20)
# 	group = models.CharField(max_length=10)
# 	photo = models.ImageField(blank=True, upload_to="photos")
	
# 	def __unicode__(self):
# 		return u'%s %s' %(self.name, self.surname)

# class Alumni(models.Model):
# 	name = models.CharField(max_length=15)
# 	surname = models.CharField(max_length=20)
# 	group = models.CharField(max_length=10)
# 	job = models.CharField(blank=True, max_length=50)
# 	licenta = models.TextField(blank=True)
# 	photo = models.ImageField(blank=True, upload_to="photos")

# 	def __unicode__(self):
# 		return u'%s %s' %(self.name, self.surname)

# class Professor(models.Model):
# 	name = models.CharField(max_length=15)
# 	surname = models.CharField(max_length=20)
# 	rank = models.CharField(max_length=30,choices=RANKINGS)
# 	photo = models.ImageField(blank=True,upload_to="photos")

# 	def __unicode__(self):
# 		return u'%s %s' %(self.name, self.surname)

# class Course(models.Model):
# 	subject_ro = models.CharField(max_length=70)
# 	subject_en = models.CharField(max_length=70)
# 	professors = models.ManyToManyField(Professor, blank=True,verbose_name="List of teachers")
# 	semester = models.IntegerField(choices=SEMESTERS)
# 	language = models.CharField(max_length=10,choices=LANGUAGES)
# 	proiectDeCurs = models.BooleanField()
# 	labs = models.BooleanField()
# 	literatura = models.TextField(blank=True)
# 	# description = models.TextField(blank=True)

# 	def __unicode__(self):
# 		return self.subject_en

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

	def __unicode__(self):
		return u'%s' % (self.key)

class UserMeta(models.Model):
	user = models.ForeignKey(User)
	meta = models.ForeignKey(UserMetaType)
	value = models.TextField()

	def __unicode__(self):
		return u'%s - %s' % (self.meta, self.value)


class UserExtended():
	def __init__(self, user_id=0):
		if user_id <= 0:
			self.user = User()
		else:
			try:
				self.user = User.objects.get(id=user_id)
			except User.DoesNotExist:
				self.user = User()
			
	def save(self):
		self.user.save()

	def delete(self):
		self.user.delete()

	def __setattr__(self, key, value):
		if key == "user":
			self.__dict__[key] = value
		elif hasattr(self.user, key):
			return setattr(self.user, key, value)
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


	def setMeta(self, key, value, unique = True):
		try:
			meta_type = UserMetaType.objects.get(key=key)
		except UserMetaType.DoesNotExist:
			print "no such meta type"
		except:
			print "error"

		try:
			user_meta = UserMeta.objects.get(user=self.user, meta=meta_type)
		except UserMeta.DoesNotExist:
			user_meta = UserMeta()
			user_meta.user = self.user
			user_meta.meta = meta_type
		except:
			print "error"

		print user_meta.id

		#TODO: check for meta_type filters
		user_meta.value = value
		user_meta.save()

	#TODO: add unique handling
	def getMeta(self, key, unique = True):
		try:
			meta_type = UserMetaType.objects.get(key=key)
		except UserMetaType.DoesNotExist:
			print "no such meta type"
		except:
			print "error"

		try:
			meta = UserMeta.objects.get(user=self.user, meta=meta_type)
			return meta.value
		except UserMeta.DoesNotExist:
			print "no such meta"
		except:
			print "error"
		
		raise AttributeError()

	def delMeta(self, key):
		try:
			meta_type = UserMetaType.objects.get(key=key)
			try:
				meta = UserMeta.objects.get(user=self.user, meta=meta_type)
				return meta.delete()
			except:
				return False
		except:
			return False

		
	

 



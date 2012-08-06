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

class UserMetaKey(models.Model):
	meta_key = models.TextField()
	meta_type = models.TextField()
	meta_data = models.TextField(blank=True)

	def __unicode__(self):
		return u'%s' % (self.meta_key)

class UserMeta(models.Model):
	user_id = models.ForeignKey(User)
	key = models.ForeignKey(UserMetaKey)
	value = models.TextField()

	def __unicode__(self):
		return u'%s - %s' % (self.key, self.value)



class DataInput():
	def __init__(self, name, surname, email, group):
		user = User(name=name, surname=surname, email=email, group=group)
		user.save()

	# def __getattr__(self, key):
	# 	try:
	# 		UserMetaKey.objects.get(meta_key=key)
	# 	except UserMetaKey.DoesNotExist:
	# 		print 'This key does not exist in the db'

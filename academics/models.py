from django.db import models

RANKINGS = (
	('LECT', 'Lecturer'),
	('LECT_SUP', 'Superior lecturer'),
	('PHD', 'PhD'),

	)

SEMESTERS = (
	('I', 'First'),
	('II', 'Second'),
	('III', 'Third'),
	('IV', 'Fourth'),
	)

LANGUAGES = (
	('EN', 'English'),
	('RO', 'Romanian'),
	)

class Student(models.Model):
	name = models.CharField(max_length=15)
	surname = models.CharField(max_length=20)
	group = models.CharField(max_length=10)
	photo = models.ImageField(blank=True, upload_to="photos")

	def __unicode__(self):
		return u'%s %s' %(self.name, self.surname)

class Alumni(models.Model):
	name = models.CharField(max_length=15)
	surname = models.CharField(max_length=20)
	group = models.CharField(max_length=10)
	photo = models.ImageField(blank=True, upload_to="photos")
	job = models.CharField(max_length=50)
	licenta = models.TextField()

	def __unicode__(self):
		return u'%s %s' %(self.name, self.surname)

class Professor(models.Model):
	name = models.CharField(max_length=15)
	surname = models.CharField(max_length=20)
	rank = models.CharField(max_length=30,choices=RANKINGS)
	photo = models.ImageField(blank=True,upload_to="photos")

	def __unicode__(self):
		return u'%s %s' %(self.name, self.surname)

class Course(models.Model):
	subject = models.CharField(max_length=50)
	professors = models.ManyToManyField(Professor, verbose_name="List of teachers")
	semester = models.IntegerField(choices=SEMESTERS)
	language = models.CharField(max_length=10,choices=LANGUAGES)
	proiectDeCurs = models.BooleanField()
	labs = models.BooleanField()
	literatura = models.TextField()
	descriere = models.TextField()

	def __unicode__(self):
		return self.subject
# Create your models here.

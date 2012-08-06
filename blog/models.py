from django.db import models
from tinymce.models import HTMLField

CONTENT_TAGS = (
	('ACT', 'Activities'),
	('ACH', 'Achievements'),
	)

class Content(models.Model):
	date = models.DateField()
	title = models.CharField(max_length=20)
	desc = HTMLField()
	tag = models.CharField(max_length=15, choices=CONTENT_TAGS)

	def __unicode__(self):
		return self.title

# Create your models here.

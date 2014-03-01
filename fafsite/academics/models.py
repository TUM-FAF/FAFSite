import json
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.db import models
from general.models import FAFUser, SEMESTERS, LANGUAGES



class Course(models.Model):
  title = models.CharField(max_length=127)
  subject_ro = models.CharField(max_length=127)
  subject_en = models.CharField(max_length=127)
  professors = models.ManyToManyField(FAFUser, blank=True,
                    verbose_name="List of professors")
  semester = models.CharField(max_length=7, choices=SEMESTERS)
  language = models.CharField(max_length=15, choices=LANGUAGES)
  courseProject = models.BooleanField()
  labs = models.BooleanField()
  literature = models.TextField(blank=True)
  description = models.TextField(blank=True)

  def __unicode__(self):
    return u'%s %s' % (self.subject_en, self.semester)

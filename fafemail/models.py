from django.db import models


class Email(models.Model):
    timestamp = models.DateTimeField()
    name = models.CharField(max_length=31, blank=True)
    email = models.EmailField()
    message = models.TextField()

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.email)

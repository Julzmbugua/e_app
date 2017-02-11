from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.

class Services(models.Model):
	errand = models.CharField(max_length =100)
	publish_date = models.DateField()

	def __str__(self):
		return self.errand



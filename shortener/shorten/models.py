import random
import string

from django.db import models

# Create your models here.

class Link(models.Model):
	key = models.CharField(max_length=5)
	url = models.URLField()

	def get_absolute_url(self):
		"""
		Make ythe url for this link
		"""
		return "http://localhost:9000/link/%s" % self.key

	def save(self, *a, **k):
		self.key = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5))
		return super(Link, self).save(*a, **k)
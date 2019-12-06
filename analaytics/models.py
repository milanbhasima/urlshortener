from django.db import models

# Create your models here.
from shortener.models import MilanUrl

class ClickEventManager(models.Manager):
	def create_event(self, instance):
		if isinstance(instance, MilanUrl):
			obj,created=self.get_or_create(milan_url=instance)
			obj.count+=1
			obj.save()
			return obj.count
		return None

class ClickEvent(models.Model):
	milan_url=models.OneToOneField(MilanUrl)
	count=models.IntegerField(default=0)
	timestamp=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)

	objects=ClickEventManager()

	def __str__(self):
		return str(self.count)
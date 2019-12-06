import random
import string
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from .validators import validate_url, validate_dot_com

SHORTCODE_MAX=getattr(settings, "SHORTCODE_MAX", 15)
SHORTCODE_MIN=getattr(settings, "SHORTCODE_MIN", 6)

def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase+ string.digits):
	# new_code=''
	# for i in range(size):
	# 	new_code += random.choice(chars)
	# return new_code
	return ''.join(random.choice(chars) for _ in range(size))
# Create your models here.

def create_shortcode(instance, size=SHORTCODE_MIN):
	new_code=code_generator(size=size)
	Klass=instance.__class__
	qs_exists=Klass.objects.filter(shortcode=new_code).exists()
	if qs_exists:
		return create_shortcode(size=size)
	return new_code

class MilanUrlManager(models.Manager):
	def all(self, *args, **kwargs):
		qs_main=super(MilanUrlManager, self).all(*args, **kwargs)
		qs=qs_main.filter(active=True)
		return qs

	def refresh_short_code(self, items=10):
		print(items)
		qs=MilanUrl.objects.filter(id__gte=1)
		if items is not None and isinstance(items, int):
			qs=qs.order_by('-id')[:items]
		new_code=0
		for q in qs:
			q.shortcode=create_shortcode(q)
			print(q.shortcode)
			q.save()
			new_code += 1
		return f"New code made :{new_code}"


class MilanUrl(models.Model):
	url=models.CharField(max_length=120, validators=[validate_url, validate_dot_com])
	shortcode=models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
	timestamp=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	active=models.BooleanField(default=True)

	objects=MilanUrlManager()

	def save(self, *args, **kwargs):
		print('hello')
		if self.shortcode is None or self.shortcode=="" or not self.shortcode:
			self.shortcode=create_shortcode(self)
		if not 'http' in self.url:
			self.url="http://" + self.url

		super(MilanUrl, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.url)

	def get_short_url(self):
		return "http://www.milan.com/{shortcode}".format(shortcode=self.shortcode)
		# return reverse('view2', kwargs={'shortcode':self.shortcode})
	def get_absolute_url(self):
		return reverse('view2', kwargs={'shortcode':self.shortcode})


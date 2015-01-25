from django.db import models
from django.utils.encoding import smart_unicode
from django.utils import timezone
from datetime import datetime
# Create your models here.
class patient(models.Model):
	firstname = models.CharField('First Name',max_length=100)
	lastname = models.CharField('Last Name', max_length=100)
	age = models.CharField('Age',max_length=5)
	mobile = models.CharField('Mobile',max_length=15)
	city = models.CharField('City',max_length=60)
	date = models.DateField('Date')
	email = models.EmailField(max_length=254)
	doctor = models.ForeignKey('doctor')
	createdat = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return smart_unicode(self.firstname)

class doctor(models.Model):
	doctorname = models.CharField(max_length=50)
	def __unicode__(self):
		return smart_unicode(self.id)

class disease(models.Model):
	patient = models.ForeignKey('patient')
	disease_symptom = models.CharField(max_length=50)
	prescription = models.CharField(max_length=50)
	reports_attacments = models.CharField(max_length=50)
	detected_disease = models.CharField(max_length=50)
	cured = models.BooleanField(default=True)
	def __unicode__(self):
		return smart_unicode(self.id)

class image(models.Model):
	patient = models.ForeignKey('patient')
	image = models.ImageField(upload_to="static/static/img/", null=True, blank=True)
	def __unicode__(self):
		return smart_unicode(self.id)

class master_admin(models.Model):
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	userid = models.CharField(max_length=50,unique=True)
	password = models.CharField(max_length=50)
	mobile = models.CharField(max_length=50)
	email=models.CharField(max_length=255)
	def __unicode__(self):
		return smart_unicode(self.id)





from django.db import models

# Create your models here.
class ProgramSave(models.Model):
	saveprogram=models.TextField()


	def __unicode__(self):
		return self.saveprogram
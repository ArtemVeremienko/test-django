from django.db import models

# Create your models here.
class Groups(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=20)
	description = models.CharField(max_length=200)

	def __str__(self):
		return self.name

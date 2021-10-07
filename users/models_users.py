from django.db import models
from users.models_groups import Groups

class Users(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	created = models.DateField(auto_now_add=True)
	group = models.ForeignKey(Groups, on_delete=models.RESTRICT)

	def __str__(self):
		return self.name

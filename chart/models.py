from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=150)
	price = models.DecimalField(max_digits=9, decimal_places=2)

	class Meta:
		verbose_name = 'Produto'
		verbose_name_plural = 'Produtos'

	def __str__(self):
		return self.name

class Person(models.Model):
	name = models.CharField(max_length=150)
	age = models.DecimalField(max_digits=3, decimal_places=1)

	class Meta:
		verbose_name = 'Person'
		verbose_name_plural = 'People'

	def __str__(self):
		return self.name
# Create your models here.

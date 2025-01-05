from django.db import models

class Brand(models.Model):
	id_brand = models.AutoField(primary_key=True)
	brand = models.CharField(max_length=30, verbose_name='Марка', default='Audi')
	class Meta:
		ordering = ['brand']
		indexes = [
			models.Index(fields=['brand']),
		]
		verbose_name = 'Марка'
		verbose_name_plural = 'Марка'	

	def __str__(self):
		return self.brand



class Product(models.Model):
	id = models.AutoField(primary_key=True)
	brand = models.ForeignKey(Brand,
		related_name='brands',
		on_delete=models.CASCADE, verbose_name = 'Марка', null=True)

	name = models.CharField(max_length=200, null=True, blank=True, verbose_name = 'Название модели')
	price = models.IntegerField(null=True, blank=True, verbose_name = 'Цена')
	price_old = models.IntegerField(null=True, blank=True, verbose_name = 'Цена БЕЗ скидки')
	noise = models.CharField(max_length=20, null=True, blank=True, verbose_name = '')
	power_max = models.CharField(max_length=20, null=True, blank=True, verbose_name = '')
	power_min = models.CharField(max_length=20, null=True, blank=True, verbose_name = '')
	work_inside = models.CharField(max_length=20, null=True, blank=True, verbose_name = '')
	work_outside = models.CharField(max_length=20, null=True, blank=True, verbose_name = '')
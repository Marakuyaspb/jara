from django.db import models

# Create your models here.
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

	name = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'ПОЛНОЕ название модели')
	variant = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Модель')
	seria = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Серия')
	power_cold = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Охлаждение, Вт')
	power_hot = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Нагрев, Вт')
	square = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Площадь, м²')
	t_cold = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Охлаждение (С°)')
	t_hot = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Нагрев (С°)')
	features = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Особенности')

	price = models.IntegerField(null=True, blank=True, verbose_name = 'Цена')
	img_1 = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name = 'Фото 1')
	img_2 = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name = 'Фото 2')
	img_3 = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name = 'Фото 3')
	img_4 = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name = 'Фото 4')
	img_5 = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name = 'Фото 5')
	img_6 = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name = 'Фото 6')
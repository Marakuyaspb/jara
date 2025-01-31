from django.db import models

class Case(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100, null=True, blank=True, verbose_name = 'Название модели')
	img_1 = models.ImageField(upload_to='portfolio/', null=True, blank=True, verbose_name = 'Фото 1')
	img_2 = models.ImageField(upload_to='portfolio/', null=True, blank=True, verbose_name = 'Фото 2')
	img_3 = models.ImageField(upload_to='portfolio/', null=True, blank=True, verbose_name = 'Фото 3')
	img_4 = models.ImageField(upload_to='portfolio/', null=True, blank=True, verbose_name = 'Фото 4')
	img_5 = models.ImageField(upload_to='portfolio/', null=True, blank=True, verbose_name = 'Фото 5')
	img_5 = models.ImageField(upload_to='portfolio/', null=True, blank=True, verbose_name = 'Фото 5')

	def __str__(self):
		return self.name
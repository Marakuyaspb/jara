from django.db import models

class Brand(models.Model):
	id_brand = models.AutoField(primary_key=True)
	brand = models.CharField(max_length=20, verbose_name='Марка', default='Haier')
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

	the_model = models.CharField(max_length=100, null=True, blank=True, verbose_name = 'Название модели')
	seria = models.CharField(max_length=150, null=True, blank=True, verbose_name = 'Серия')

	price = models.IntegerField(null=True, blank=True, verbose_name = 'Цена')
	price_old = models.IntegerField(null=True, blank=True, verbose_name = 'Цена БЕЗ скидки')

	power_cold = models.CharField(max_length=20, null=True, blank=True, verbose_name = 'Охлаждение, Вт')
	power_warm = models.CharField(max_length=20, null=True, blank=True, verbose_name = 'Нагрев, Вт')
	square = models.CharField(max_length=20, null=True, blank=True, verbose_name = 'Площадь')
	temp_cold = models.CharField(max_length=20, null=True, blank=True, verbose_name = 'Охлаждение (С°)')
	temp_warm = models.CharField(max_length=20, null=True, blank=True, verbose_name = 'Нагрев (С°)')
	features = models.TextField(null=True, blank=True, verbose_name = 'Особенности')

	img_1 = models.ImageField(upload_to='catalog/', null=True, blank=True, verbose_name = 'Фото 1')
	img_2 = models.ImageField(upload_to='catalog/', null=True, blank=True, verbose_name = 'Фото 2')
	img_3 = models.ImageField(upload_to='catalog/', null=True, blank=True, verbose_name = 'Фото 3')
	img_4 = models.ImageField(upload_to='catalog/', null=True, blank=True, verbose_name = 'Фото 4')
	img_5 = models.ImageField(upload_to='catalog/', null=True, blank=True, verbose_name = 'Фото 5')
	
	def __str__(self):
		return self.name



class CallMe(models.Model):
	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=30)
	phone = models.CharField(max_length=30)
	created = models.DateTimeField(auto_now_add=True, verbose_name = 'Заявка поступила')

	class Meta:
		ordering = ['-created']
		verbose_name = 'Заявка: перезвоните мне'
		verbose_name_plural = 'Заявки: перезвоните мне'
	def __str__(self):
		return self.first_name



class WantThis(models.Model):
	id = models.AutoField(primary_key=True)
	the_model = models.CharField(max_length=50, verbose_name = 'Марка машины')
	first_name = models.CharField(max_length=30, verbose_name = 'Имя')
	phone = models.CharField(max_length=30, verbose_name = 'Телефон')
	created = models.DateTimeField(auto_now_add=True, verbose_name = 'Заявка поступила')
	
	class Meta:
		ordering = ['-created']
		verbose_name = 'Хочу такой же'
		verbose_name_plural = 'Запросы: хочу такой же!'

	def __str__(self):
		return self.first_name



class FixIt(models.Model):
	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=30)
	phone = models.CharField(max_length=30, null=True, blank=True)
	problem = models.TextField()
	created = models.DateTimeField(auto_now_add=True, verbose_name = 'Заявка поступила')

	class Meta:
		ordering = ['-created']
		verbose_name = 'Заявка: перезвоните мне'
		verbose_name_plural = 'Заявки: перезвоните мне'
	def __str__(self):
		return self.first_name

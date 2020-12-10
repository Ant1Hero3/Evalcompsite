from django.db import models
from django.utils import timezone

# Create your models here.
class Application(models.Model):
	last_name = models.CharField(max_length = 255, verbose_name="Фамилия")
	first_name = models.CharField(max_length = 255, verbose_name="Имя")
	patronymic = models.CharField(max_length = 255, blank=True, verbose_name="Отчество")
	email = models.CharField(max_length = 255, verbose_name="Электронный адрес")
	phone_number = models.CharField(blank=False, max_length = 255, verbose_name="Номер телефона")
	eval_object = models.CharField(max_length = 255, verbose_name="Объект оценки")
	aim = models.CharField(max_length = 255, verbose_name="Цель оценки")
	address = models.CharField(max_length = 255, verbose_name="Адрес объекта оценки")
	price = models.IntegerField(verbose_name="Цена покупки")
	comment = models.CharField(max_length = 255, blank=True, verbose_name="Комментарии")
	date = models.DateTimeField(default=timezone.now, verbose_name="Дата заявки")

	class Meta:
		verbose_name = 'Заявка'
		verbose_name_plural = 'Заявки'

class Apartment(models.Model):
	location = models.CharField(max_length = 255, verbose_name="Местоположение")
	price = models.CharField(max_length = 255, verbose_name="Стоимость услуг")

	class Meta:
		verbose_name = 'Квартира'
		verbose_name_plural = 'Квартиры'

class House(models.Model):
	location = models.CharField(max_length = 255, verbose_name="Местоположение")
	price = models.CharField(max_length = 255, verbose_name="Стоимость услуг")

	class Meta:
		verbose_name = 'Дом'
		verbose_name_plural = 'Дома'

class Land(models.Model):
	location = models.CharField(max_length = 255, verbose_name="Местоположение")
	price = models.CharField(max_length = 255, verbose_name="Стоимость услуг")

	class Meta:
		verbose_name = 'Земельный участок'
		verbose_name_plural = 'Земельные участки'

class Comment(models.Model):
	name = models.CharField(max_length = 255, verbose_name="Имя")
	comment = models.CharField(max_length = 255, blank=True, verbose_name="Комментарии")
	date = models.DateTimeField(default=timezone.now, verbose_name="Дата заявки")

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'	

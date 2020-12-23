

from django.db import models
from datetime import datetime
# Create your models here.


class Owner(models.Model):
    class Meta:
        db_table = 'owner'
        verbose_name = 'владелец'
        verbose_name_plural = 'владелецы'
        ordering = ('name',)

    name = models.CharField(max_length=25, verbose_name='имя')
    first_name = models.CharField(max_length=25, verbose_name='фамиля')
    age = models.IntegerField(verbose_name='возраст')
    date = models.DateTimeField(default=datetime.now, verbose_name='дата')

    def __str__(self):
        return self.name


class Animals(models.Model):
    class Meta:
        db_table = 'animal'
        verbose_name = 'жывотни'
        verbose_name_plural = 'животные'
        ordering = ('name',)

    name = models.CharField(max_length=30, verbose_name='название')
    age = models.IntegerField(verbose_name='возраст')
    description = models.CharField(max_length=300, verbose_name='описание')
    type = models.CharField(max_length=20, verbose_name='тып')
    photo = models.ImageField('Фото', upload_to='owner/photos', default='', blank=True)
    owner_animals = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='animal')

    def __str__(self):
        return self.name



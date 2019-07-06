from django.db import models

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.category


class Hobby(models.Model):
    hobby = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, default=1, verbose_name='Category', on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural = 'Hobby'

    def __str__(self):
        return self.hobby


class Name(models.Model):
    name = models.CharField(max_length=100)
    hobby = models.ForeignKey(
        Hobby, default=1, verbose_name='Hobby', on_delete=models.SET_DEFAULT)
    category = models.ForeignKey(
        Category, default=1, verbose_name='Category', on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural = 'Name'

    def __str__(self):
        return self.name

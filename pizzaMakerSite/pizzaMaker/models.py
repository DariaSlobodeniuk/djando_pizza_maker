from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)



class TypeIngredient(models.Model):

    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = "TypeIngredient"
        verbose_name_plural = "TypeIngredients"


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    idTypeIngredients = models.ForeignKey(TypeIngredient, related_name='TypeIngredient', on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"


class Pizza(models.Model):

    idIngredient = models.ManyToManyField(Ingredient, related_name='Ingredient')
    amount = models.IntegerField()
    # price = models.FloatField(Ingredient.price)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Pizza"
        verbose_name_plural = "Pizzas"
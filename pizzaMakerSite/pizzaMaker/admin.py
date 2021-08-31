from django.contrib import admin
from .models import TypeIngredient, Ingredient, Pizza


admin.site.register(TypeIngredient)
admin.site.register(Ingredient)
admin.site.register(Pizza)
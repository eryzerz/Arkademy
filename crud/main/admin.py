from django.contrib import admin
from .models import Name, Hobby, Category
# Register your models here.
admin.site.register(Name)
admin.site.register(Hobby)
admin.site.register(Category)

from django.contrib import admin
from .models import Category, Dish, Event, Banners, UsersMessages

# Register your models here.
admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Event)
admin.site.register(Banners)
admin.site.register(UsersMessages)

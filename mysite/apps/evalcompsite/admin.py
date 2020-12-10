from django.contrib import admin

from .models import Application, Apartment, House, Land, Comment

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
	list_display=('id', 'last_name', 'first_name', 'patronymic', 'email', 'phone_number', 'eval_object', 'aim', 'address', 'price', 'comment', 'date')

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
	list_display=('location', 'price')

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
	list_display=('location', 'price')

@admin.register(Land)
class LandAdmin(admin.ModelAdmin):
	list_display=('location', 'price')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display=('id', 'name', 'comment', 'date')

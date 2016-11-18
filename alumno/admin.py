from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _

from . import models

class UserProfileInline(admin.StackedInline):
	model = models.Alumno
	can_delete = False

class MyUserAdmin(BaseUserAdmin):

	class Meta:
		email = {
			'required': True
		}

	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name',)}
		),
	)
	inlines = (UserProfileInline,)

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)



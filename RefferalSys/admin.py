from django.contrib import admin
from .models import UserProfile, AuthenticationCode


@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(AuthenticationCode)
class AuthAdmin(admin.ModelAdmin):
    pass
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Company, User


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('company',)}),)
    list_display = ('username', 'email', 'company', 'is_staff')

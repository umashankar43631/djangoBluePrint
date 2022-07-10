from django.contrib import admin
from .models import Login
# Register your models here.
class LoginAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("username",)}

admin.site.register(Login, LoginAdmin)
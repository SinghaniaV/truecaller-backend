from django.contrib import admin

from .models import Identity, Registered, RegisteredToSaved

# Register your models here.

admin.site.register(Identity)
admin.site.register(Registered)
admin.site.register(RegisteredToSaved)

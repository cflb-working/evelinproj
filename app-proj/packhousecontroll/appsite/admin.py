from django.contrib import admin
from .models import Client, Address, Annotation

# Register your models here.
admin.site.register(Client)
admin.site.register(Address)
admin.site.register(Annotation)
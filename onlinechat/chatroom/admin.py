from django.contrib import admin

from .models import User, Contacts, Chat

# Register your models here.
admin.site.register(User)
admin.site.register(Contacts)
admin.site.register(Chat)

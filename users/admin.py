from django.contrib import admin

from .models import MyUser, Payment


admin.site.register(MyUser)

admin.site.register(Payment)


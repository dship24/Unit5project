from django.contrib import admin

from app.models import *

admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Order)
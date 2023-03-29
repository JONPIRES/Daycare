from django.contrib import admin

# Register your models here.
from .models import Kids, Feeding

# Register your models here
admin.site.register(Kids)
admin.site.register(Feeding)
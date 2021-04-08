from django.contrib import admin
from .models import product
from .models import category

admin.site.register(product)
admin.site.register(category)
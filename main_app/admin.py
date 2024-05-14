from django.contrib import admin
from .models import Spren, Feeding, Power, Radiant, Interaction

# Register your models here.

admin.site.register(Spren)
admin.site.register(Feeding)
admin.site.register(Power)
admin.site.register(Radiant)
admin.site.register(Interaction)
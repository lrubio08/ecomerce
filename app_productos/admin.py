from django.contrib import admin
from .models import Smartphone, Notebook, Tablet, PcEscritorio, Televisor


admin.site.register(Smartphone)
admin.site.register(Notebook)
admin.site.register(Tablet)
admin.site.register(PcEscritorio)
admin.site.register(Televisor)
from django.contrib import admin
from .models import Gen


class GenAdmin(admin.ModelAdmin):
    list_display = ('ily_text',)


admin.site.register(Gen, GenAdmin)

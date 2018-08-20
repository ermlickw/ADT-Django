from django.contrib import admin

from .models import  Claim, File


admin.site.register(File)
admin.site.register(Claim)

from django.contrib import admin

from .models import  Claim, Nothing, File


admin.site.register(File)
admin.site.register(Claim)
admin.site.register(Nothing)

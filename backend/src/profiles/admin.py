from django.contrib import admin
from .models import ATSUser, Gender, VController, Division, Position

# Register your models here.
admin.site.register(Gender)
admin.site.register(VController)
admin.site.register(Division)
admin.site.register(Position)
admin.site.register(ATSUser)
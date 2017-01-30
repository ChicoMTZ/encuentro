from django.contrib import admin
from .models import *
# Register your models here.

#
admin.site.register(Profile)
# class PersonAdmin(admin.ModelAdmin):
#     def get_queryset(self, request):
#         qs = super(PersonAdmin, self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(usuario=request.user)

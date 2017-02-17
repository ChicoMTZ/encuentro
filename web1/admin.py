from django.contrib import admin
<<<<<<< HEAD

# Register your models here.

#
=======
from .models import *
# Register your models here.


@admin.register(Article)
class PersonAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(PersonAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario=request.user)
>>>>>>> bd03b5de37d4106749cf9ce989d13228f5e5bcf6

from django.contrib import admin

# Register your models here.
from contact.models import Contact

class contactAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'phone', 'message')


admin.site.register(Contact, contactAdmin)



from django.contrib import admin
from .models import Phonesmode, offer


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')

class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

admin.site.register(Phonesmode, PhoneAdmin)
admin.site.register(offer, OfferAdmin )

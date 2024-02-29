from django.contrib import admin
from .models import Card, Delivered, DeliveryException, Pickup, Returned
# Register your models here.
admin.site.register(Card)
admin.site.register(Delivered)
admin.site.register(DeliveryException)
admin.site.register(Pickup)
admin.site.register(Returned)
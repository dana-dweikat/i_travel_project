from django.contrib import admin
from .models import *

admin.site.register(Guest)
admin.site.register(Hotel)
admin.site.register(Package)
admin.site.register(Event)
admin.site.register(PackageEvent)
admin.site.register(HotelPackages)
admin.site.register(Bill)
admin.site.register(Booking)
admin.site.register(FeedBack)

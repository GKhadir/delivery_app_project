from django.contrib import admin
from .models import UsersData,user_profiles,delivary_partner_details,addresses
# Register your models here.
admin.site.register(UsersData)
admin.site.register(user_profiles)
admin.site.register(delivary_partner_details)
admin.site.register(addresses)
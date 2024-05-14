from django.contrib import admin
from .models import Bill, Cloth, Food, Travel, Subscription, Miscellaneous

admin.site.register(Bill)
admin.site.register(Cloth)
admin.site.register(Food)
admin.site.register(Travel)
admin.site.register(Subscription)
admin.site.register(Miscellaneous)
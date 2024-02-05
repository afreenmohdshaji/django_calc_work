from django.contrib import admin
from scrapboxapp.models import Scrap,Category,UserProfile,Bids

# Register your models here.

admin.site.register(Scrap)
admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Bids)
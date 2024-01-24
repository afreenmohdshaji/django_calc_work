from django.contrib import admin
from scrapboxapp.models import Scrap,Category,UserProfile

# Register your models here.

admin.site.register(Scrap)
admin.site.register(Category)
admin.site.register(UserProfile)
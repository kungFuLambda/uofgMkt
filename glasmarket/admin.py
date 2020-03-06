from django.contrib import admin
from glasmarket.models import User,Listing,Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin): 
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(User)
admin.site.register(Listing)
from django.contrib import admin
from .models import Item,Order,Category,ItemQuantity
# Register your models here.
class ChoiceInline(admin.TabularInline):
    model=ItemQuantity
    extra=1

class OrderAdmin(admin.ModelAdmin):
    #fields=['pub_date','question_text']
    inlines=[ChoiceInline]


admin.site.register(Item)
admin.site.register(Order,OrderAdmin)
admin.site.register(Category)
admin.site.register(ItemQuantity)
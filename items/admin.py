from django.contrib import admin

# Register your models here.
from items.forms import ItemForm
from items.models import Item


class ItemAdmin(admin.ModelAdmin):
    form = ItemForm

    search_fields = ('name', 'code')

    list_display = (
        'name',
        'code',
        'description',
        'cost',
    )

    readonly_fields = (
        'code',
    )

    fieldsets = (
        ('ItemCode', {
            'fields': ['code']
        }),
        ('Item', {
            'fields': ('name', 'description', 'cost')
        }),
    )


admin.site.register(Item, ItemAdmin)

import random

from allauth.socialaccount.models import SocialAccount, SocialToken, SocialApp
from django.contrib import admin
from django.contrib.sites.models import Site

from product.models import Item, ItemPhoto, Category


class ItemPhotoInline(admin.TabularInline):
    model = ItemPhoto
    extra = 0


class ItemAdmin(admin.ModelAdmin):
    """Add photos to Item in Admin"""
    inlines = [ItemPhotoInline]
    list_display = ('sku', '__str__', 'status', 'category',)
    list_filter = ('category',)
    search_fields = ('sku',)
    readonly_fields = ('sku',)

    def save_model(self, request, obj, form, change):
        """Add SKU to Item."""
        super().save_model(request, obj, form, change)
        if not obj.sku:
            obj.sku = str(obj.id) + str(random.randint(100, 999))
            obj.save()


admin.site.register(Item, ItemAdmin)
admin.site.register(Category)

admin.site.unregister(SocialAccount)
admin.site.unregister(SocialToken)
admin.site.unregister(SocialApp)
admin.site.unregister(Site)

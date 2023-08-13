import admin_thumbnails
from django.contrib import admin
from django.db import IntegrityError
from .models import Category, Product, Images, Color, Size, Variants


def duplicate_product(self, request, queryset):
    try:
        for product in queryset:
            product.pk = None
            product.id = None
            product.name += " Copy"
            product.slug += "-copy"
            product.save()
        self.message_user(
            request, "Selected products have been duplicated successfully.")
    except IntegrityError:
        self.message_user(
            request, "Error: Duplicated slug found. Selected products were not duplicated.")


duplicate_product.short_description = "Duplicate selected products"


@admin_thumbnails.thumbnail('image')
class ProductImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 1


class ProductVariantsInline(admin.TabularInline):
    model = Variants
    readonly_fields = ('image_tag',)
    extra = 1
    show_change_link = True


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'parent']
    list_filter = ['name', 'status',]
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ['name', 'parent']
    search_fields = ['name', 'parent']
    list_per_page = 25


@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image', 'name', 'image_thumbnail', ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'status',
                    'price', 'stock', 'compare_price', 'image_tag']
    list_filter = ['status', 'category', 'stock',]
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']
    list_per_page = 25
    list_editable = ('compare_price', 'price', 'stock', "status", )
    actions = [duplicate_product]
    inlines = [ProductImageInline, ProductVariantsInline]


class ColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'color_tag']
    list_editable = ('code',)


class SizeAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']
    prepopulated_fields = {'code': ('name',)}
    list_editable = ('code',)


class VariantsAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_id', 'image_tag']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Variants, VariantsAdmin)

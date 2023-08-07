import admin_thumbnails
from django.contrib import admin
from .models import Category, Product, Images, Color, Size, Variants


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
    list_display = ['image', 'name', 'image_thumbnail']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'status',
                    'price', 'stock', 'compare_price', 'image_tag']
    list_filter = ['status', 'category', 'stock',]
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']
    list_per_page = 25
    list_editable = ('compare_price', 'price', 'stock', "status", )
    inlines = [ProductImageInline, ProductVariantsInline]


class ColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'color_tag']
    list_editable = ('code',)


class SizeAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']
    prepopulated_fields = {'code': ('name',)}
    list_editable = ('code',)


class VariantsAdmin(admin.ModelAdmin):
    list_display = ['name', 'product', 'color',
                    'size', 'price', 'quantity', 'image_tag']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Variants, VariantsAdmin)

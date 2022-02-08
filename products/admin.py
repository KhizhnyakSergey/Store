from django.contrib import admin
from products.models import ProductCategory, Product, Basket, Slider

from django.utils.safestring import mark_safe
# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Basket)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category', 'get_img')
    fields = ('name', ('get_img', 'image'), 'description', 'short_description', 'price', 'quantity', 'category')
    # readonly_fields = ('short_description',)
    ordering = ('name',)
    search_fields = ('name',)
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="60px"')
        else:
            return 'нет картинки'

    get_img.short_description = 'Миниатюра'


class BasketAdminInline(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('product', 'created_timestamp',)
    extra = 0


# моё добавление
@admin.register(Slider)
class ProductSlider(admin.ModelAdmin):
    list_display = ('title', 'css', 'get_img')
    list_display_links = ('title',)
    list_editable = ('css',)
    fields = ('title', 'css', 'img', 'get_img')
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" width="150px"')
        else:
            return 'нет картинки'

    get_img.short_description = 'Миниатюра'

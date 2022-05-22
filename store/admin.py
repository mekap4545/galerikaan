from django.contrib import admin
from .models import Product, ProductGallery
import admin_thumbnails

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('başlık', 'tarih', 'marka', 'seri', 'model', 'yıl', 'yakıt', 'vites', 'km', 'kasatipi', 'motorgucu', 'motorhacmi', 'çekiş', 'renk', 'garanti', 'plaka', 'kimden', 'takas', 'durumu', 'boya', 'degisen', 'guvenlik', 'icdonanim', 'dişdonanım', 'multimedya',   'fiyat', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('başlık',)}
    inlines = [ProductGalleryInline]
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGallery)
 
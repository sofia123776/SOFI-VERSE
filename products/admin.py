from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'stock',
        'available',
        'featured'
    )

    list_filter = (
        'available',
        'featured',
        'category'
    )

    prepopulated_fields = {
        'slug': ('name',)
    }
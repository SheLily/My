from django.contrib import admin

from shop.models import Product, Tag, Cart, Review, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'description',
        'image',
        'tag',
    ]
    list_filter = [
        'tag',
    ]
    search_fields = [
        'name',
        'price',
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
    ]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = [
        'user',
    ]
    search_fields = [
        'user',
    ]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        'product',
        'author',
        'body',
        'rating',
    ]
    list_filter = [
        'product',
        'rating',
    ]
    search_fields = [
        'product',
        'author',
        'body',
        'rating',
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'owner',
    ]
    list_filter = [
        'owner',
    ]
    search_fields = [
        'owner',
    ]

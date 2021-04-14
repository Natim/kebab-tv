from django.contrib import admin

from .models import Category, Product, Screen


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    order_by = ("category__pk", "name")
    list_filter = ["category"]
    search_fields = ["name", "category__name"]


admin.site.register(Screen)
admin.site.register(Category)

from django.contrib import admin

from admin_ordering.admin import OrderableAdmin

from .models import Category, Product, Screen


@admin.register(Product)
class ProductAdmin(OrderableAdmin, admin.ModelAdmin):
    ordering = ("category__ordering", "ordering")

    list_display = ("name", "category", "ordering")
    order_by = ("category__pk", "name")
    list_filter = ["category"]
    search_fields = ["name", "category__name"]
    list_editable = ["ordering"]


@admin.register(Screen)
class ScreenAdmin(OrderableAdmin, admin.ModelAdmin):
    ordering = ("ordering",)

    # You may optionally hide the ordering field in the changelist:
    # ordering_field_hide_input = False

    # The ordering field must be included both in list_display and
    # list_editable:
    list_display = ["name", "ordering"]
    list_editable = ["ordering"]

@admin.register(Category)
class CategoryAdmin(OrderableAdmin, admin.ModelAdmin):
    ordering = ("ordering",)

    # You may optionally hide the ordering field in the changelist:
    # ordering_field_hide_input = False

    # The ordering field must be included both in list_display and
    # list_editable:
    list_display = ["name", "ordering"]
    list_editable = ["ordering"]

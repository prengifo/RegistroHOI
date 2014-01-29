from django.contrib import admin
from django.db.models import Count, Min, Sum, Avg
from django import forms
from models import *


class ItemChangeAdminForm(forms.ModelForm):
    class Meta:
        model = ItemChange

    def clean_delta(self):
        # do something that validates your data
        delta = self.cleaned_data["delta"]
        if not self.instance.pk or self.instance.delta != delta:
            item = self.cleaned_data['item']
            s = delta+ItemChange.objects.filter(item=item).aggregate(inventario=Sum('delta'))['inventario']
            if s < 0:
                raise forms.ValidationError("No hay suficiente material para tomar esa cantidad!")
        return delta

class ItemChangeInline(admin.TabularInline):
    model = ItemChange
    form = ItemChangeAdminForm


# class IsOutListFilter(SimpleListFilter):
#     title = _('filtrar por inventario')
#     parameter_name = 'is_out'

#     def lookups(self, request, model_admin):
#         """
#         Returns a list of tuples. The first element in each
#         tuple is the coded value for the option that will
#         appear in the URL query. The second element is the
#         human-readable name for the option that will appear
#         in the right sidebar.
#         """
#         return (
#             ('true', _('queda en existencia')),
#             ('false', _('no queda en existencia')),
#         )

#     def queryset(self, request, queryset):
#         """
#         Returns the filtered queryset based on the value
#         provided in the query string and retrievable via
#         `self.value()`.
#         """
#         # Compare the requested value (either '80s' or '90s')
#         # to decide how to filter the queryset.
#         if self.value() == 'true':
#             return queryset.filter(birthday__gte=date(1980, 1, 1),
#                                     birthday__lte=date(1989, 12, 31))
#         if self.value() == 'false':
#             return queryset.filter(birthday__gte=date(1990, 1, 1),
#                                     birthday__lte=date(1999, 12, 31))

class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_code', 'name', 'inventario','cost', 'costo_total',]
    list_display_links = ['item_code', 'name']
    list_filter = ['is_out']
    search_fields = ['name', 'item_code',]
    inlines = [ItemChangeInline,]
    exclude = ['is_out',]

admin.site.register(Item, ItemAdmin)
# admin.site.register(ItemChange)

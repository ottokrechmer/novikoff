from django.contrib import admin

from core.services.roszdrav.integration import ImportData


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address_region', 'ogrn', 'inn')
    search_fields = ('name', 'address_region', 'ogrn', 'inn')
    list_filter = ('address_region',)
    actions = ('import_all_data',)

    @admin.action(description='Импорт')
    def import_all_data(self, request, queryset):
        idata = ImportData()
        idata.parse()

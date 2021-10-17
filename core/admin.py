from django.contrib import admin

from core.admin_classes.organization_admin import OrganizationAdmin
from core.models import Organization

admin.site.register(Organization, OrganizationAdmin)

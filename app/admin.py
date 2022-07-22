from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ['fullname', 'email', 'title', 'text', 'datetime_created', 'datetime_answered', 'is_answered']
    list_display = ['fullname', 'email', 'title', 'is_answered', 'datetime_answered']
    list_filter = ['is_answered']

    def has_add_permission(self, request):
        return False

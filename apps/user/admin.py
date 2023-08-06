from django.contrib import admin
from django.contrib.auth import get_user_model


User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',
                    'is_staff', 'is_superuser', 'is_active', 'last_login')
    list_display_links = ('first_name', 'last_name', 'email', )
    search_fields = ('first_name', 'last_name', 'email',
                     'is_staff', 'is_superuser', 'is_active', 'last_login')
    list_per_page = 25
    ordering = ('-date_joined',)
    readonly_fields = ('last_login', 'date_joined')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, UserAdmin)

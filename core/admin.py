from django.contrib import admin

from core.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # fields = ('__all__', )
    list_display = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    readonly_fields = ('last_login', 'date_joined', )


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from base.forms import UserCreationForm
from base.models import User, Profile, Nippou
from base.models.output import Output

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password',
            )
        }),
        (None, {
            'fields': (
                'date_joined',
                'username',
                'is_active',
                'is_admin',
            )
        })
    )
    list_display = ('username', 'is_active')
    list_filter = ()
    ordering = ()
    filter_horizontal = ()

    # --- adminでuser作成用に追加 ---
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password',),
        }),
    )
    # --- adminでuser作成用に追加 ---

    add_form = UserCreationForm

admin.site.register(User, CustomUserAdmin)
admin.site.register(Nippou)
admin.site.register(Output)
from django.contrib import admin
from DataAccessLayer.User.model import User
from django.contrib.auth.admin import UserAdmin
from DataAccessLayer.ContactGroup.model import ContactGroup
from DataAccessLayer.Contact.model import Contact


class UserAdminConfig(UserAdmin):
    ordering = ['-created_at']
    list_display = ('first_name', 'last_name', 'is_active', 'email', 'created_at')
    search_fields = ('email', 'first_name', 'last_name')
    fieldsets = (
        ('Personal info', {'fields': ('first_name', 'middle_name', 'last_name', 'gender', 'email')}),
        ('Status', {'fields': ('is_active',)})
    )
    add_fieldsets = (
        ('Personal info', {
            'classes': ('wide',),
            'fields': ('first_name', 'middle_name', 'last_name', 'email')
        }),
        ('Security', {
            'classes': ('wide',),
            'fields': ('password1', 'password2', 'is_active')
        })
    )


admin.site.register(User, UserAdminConfig)
admin.site.register(Contact)
admin.site.register(ContactGroup)

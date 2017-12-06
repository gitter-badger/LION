from django.contrib import admin
from accounts.models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.

def make_is_staff(modeladmin, request, queryset):
    queryset.update(is_staff=True)        

make_is_staff.short_description = (u"スタッフ権限を与える")

def unmake_is_staff(modeladmin, request, queryset):
    queryset.update(is_staff=False)

unmake_is_staff.short_description = (u"スタッフ権限をはく奪する")

class UserCustomedAdmin(UserAdmin):
    list_display=(
        "username", "last_name", "first_name", "last_name_kana", "first_name_kana", "is_staff"
    )

    search_fields = [
        "username", "last_name", "first_name", "last_name_kana", "first_name_kana", "email"
    ]
    fieldsets = UserAdmin.fieldsets + (
        ("追加情報", {'fields': ('telephone', 'faculty', 'grade')}),
    )

    list_filter=[
        "is_staff"
    ]

    actions = [make_is_staff, unmake_is_staff]
admin.site.register(User, UserCustomedAdmin)
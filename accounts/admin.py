from django.contrib import admin
from accounts.models import User


# Register your models here.

def make_is_staff(modeladmin, request, queryset):
    queryset.update(is_staff=True)        

make_is_staff.short_description = (u"スタッフ権限を与える")

def unmake_is_staff(modeladmin, request, queryset):
    queryset.update(is_staff=False)

unmake_is_staff.short_description = (u"スタッフ権限をはく奪する")

class UserAdmin(admin.ModelAdmin):
    list_display=(
        "username", "last_name", "first_name", "is_staff"
    )

    fieldsets = [
        ("ログイン情報", {"fields": ["username"]}),
        ("基本情報", {'fields': ["last_name", "first_name", "last_name_kana", "first_name_kana", "faculty", "grade"]}),
        ("連絡先", {"fields": ["email", "telephone"]}),
        ("権限情報（不用意にいじらないこと！）", {"fields": ["is_staff", "is_active"]})
    ]

    list_filter=[
        "is_staff"
    ]

    actions = [make_is_staff, unmake_is_staff]
admin.site.register(User, UserAdmin)
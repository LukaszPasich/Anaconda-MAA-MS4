from django.contrib import admin
from .models import Membership


class MembershipAdmin(admin.ModelAdmin):
    list_display = (
        'membership_no',
        'name',
        'small_name',
        'price',
        'pay_interval',
    )

    ordering = ('membership_no',)


admin.site.register(Membership, MembershipAdmin)

from django.contrib import admin
from .models import Membership, Discipline


class DisciplineAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )

class MembershipAdmin(admin.ModelAdmin):
    list_display = (
        'membership_no',
        'name',
        'small_name',
        'all_classes',
        'price',
        'pay_interval',
    )

    ordering = ('membership_no',)


admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Membership, MembershipAdmin)

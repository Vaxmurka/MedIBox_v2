from django.contrib import admin
from .models import Groups, Patient, Voices, Schedule, Pills, TakingPills


@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    # list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    # list_display = ('first_name', 'username', 'fingerprint', 'number')
    # list_filter = ['available', 'created', 'updated']
    prepopulated_fields = {'slug': ('fingerprint',)}


admin.site.register(Voices, admin.ModelAdmin)
admin.site.register(Schedule, admin.ModelAdmin)
admin.site.register(Pills, admin.ModelAdmin)
admin.site.register(TakingPills, admin.ModelAdmin)

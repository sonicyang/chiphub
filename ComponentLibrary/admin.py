from django.contrib import admin
from ComponentLibrary.models import GComponents, GClasses

class ComponentInline(admin.TabularInline):
    model = GComponents
    extra = 1

@admin.register(GComponents)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ('common_name', 'manufacturer','ctype')

@admin.register(GClasses)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('mname', 'sname')

    inlines = [ComponentInline]

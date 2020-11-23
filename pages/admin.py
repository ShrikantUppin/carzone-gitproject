from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.


# admin page customization

class TeamAdmin(admin.ModelAdmin):

    def thumbnil(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px"/>'.format(object.photo.url))

    thumbnil.short_description = 'photo'
    list_display = ('id', 'thumbnil', 'first_name', 'designation','created_date')
    list_display_links = ('id','thumbnil','first_name',)
    search_fields = ('id', 'first_name', 'last_name', 'designation')
    list_filter = ('designation',)


admin.site.register(Team, TeamAdmin)

from django.contrib import admin
from .models import Profile, Experience, SocialLink, ContactInfo


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'specialty', 'years_of_experience', 'projects_count')
    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('full_name', 'specialty', 'photo', 'years_of_experience', 'projects_count')
        }),
        ('Bio', {
            'fields': ('bio',)
        }),
        ('Harakat tugmasi', {
            'fields': ('work_together_url',),
            'description': 'Birga ishlash tugmasi bosilganda qayerga yo\'naltirish kerak.'
        }),
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('year', 'title', 'order')
    list_editable = ('order',)
    ordering = ('order', 'year')


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'platform', 'url', 'order')
    list_editable = ('order',)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'email')


# Admin panel sarlavhalarini o'zgartirish
admin.site.site_header = "Safobek Portfolio – Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Boshqaruv paneli"

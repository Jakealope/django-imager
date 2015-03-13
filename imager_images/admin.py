from django.contrib import admin
from imager_images.models import Album, Photo
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class ImagerProfileInline(admin.StackedInline):
    model = Album, Photo
    can_delete = False
    verbose_name_plural = 'imager albums'


class UserAdmin(UserAdmin):
    inlines = (ImagerProfileInline, )


admin.site.register(Album)
admin.site.register(Photo)

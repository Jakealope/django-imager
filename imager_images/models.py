from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Photo(models.Model):
    picture = models.ImageField(upload_to='photos')
    user = models.ForeignKey(User, related_name='photo')
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    date_uploaded = models.DateField(auto_now_add=True, null=True, blank=True)
    date_modified = models.DateField(auto_now=True, null=True, blank=True)
    date_publishd = models.DateField(null=True, blank=True)

    PRIVATE = 'private'
    SHARED = 'shared'
    PUBLIC = 'public'
    PHOTO_PRIVACY_OPTIONS = (
        (PRIVATE, 'private', ),
        (SHARED, 'shared', ),
        (PUBLIC, 'public', ),
    )

    PUBLISHED = models.CharField(
        max_length=10,
        choices=PHOTO_PRIVACY_OPTIONS,
        default=PRIVATE
    )

    def __str__(self):
        return str(self.title)


@python_2_unicode_compatible
class Album(models.Model):
    user = models.ForeignKey(User, related_name='album')
    pictures = models.ManyToManyField(
        Photo,
        related_name='album',
        # limit_choices_to={user: 'self'}
    )
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)
    date_modified = models.DateField(auto_now=True, null=True, blank=True)
    date_publishd = models.DateField(null=True, blank=True)

    PRIVATE = 'private'
    SHARED = 'shared'
    PUBLIC = 'public'
    ALBUM_PRIVACY_OPTIONS = (
        (PRIVATE, 'private', ),
        (SHARED, 'shared', ),
        (PUBLIC, 'public', ),
    )

    PUBLISHED = models.CharField(
        max_length=10,
        choices=ALBUM_PRIVACY_OPTIONS,
        default=PRIVATE
    )

    cover = models.ForeignKey(Photo, blank=True, related_name='+', null=True)

    def get_cover_photo(self):
        if self.photo_set.filter(is_cover_photo=True).count() > 0:
            return self.photo_set.filter(is_cover_photo=True)[0]
        elif self.photo_set.all().count() > 0:
            return self.photo_set.all()[0]
        else:
            return None

    def __str__(self):
        return str(self.title)

# @python_2_unicode_compatible
# class Album_Admin(admin.ModelAdmin):
#     search_fields = ["title"]
#     list_display = ["title"]

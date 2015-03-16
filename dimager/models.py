from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.encoding import python_2_unicode_compatible
from django.core.files.uploadedfile import SimpleUploadedFile
import os
from PIL import Image
from cStringIO import StringIO


class ActiveImagerManager(models.Manager):
    '''Return active users, inherit query set'''
    def get_queryset(self):
        qs = super(ActiveImagerManager, self).get_queryset()
        return qs.filter(user__is_active__exact=True)


@python_2_unicode_compatible
class ImagerProfile(models.Model):
    '''Expanding user profile'''

    user = models.OneToOneField(User, related_name='profile')
    following = models.ManyToManyField(
        'self', related_name='_following', symmetrical=False)
    blocking = models.ManyToManyField(
        'self', related_name='_blocking', symmetrical=False)
    picture = models.ImageField(
        upload_to='profile_image', blank=True, max_length=100)
    picture_privacy = models.BooleanField(default=True)

    birthday = models.DateField('date of birth', null=True)
    birthday_privacy = models.BooleanField(default=True)

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message=(
            "Entered in the format: '+999999999'. Up to 15 digits allowed."))
    phone_number = models.CharField(
        validators=[phone_regex], blank=True, max_length=15)
    phone_privacy = models.BooleanField(default=True)

    name_privacy = models.BooleanField(default=True)
    email_privacy = models.BooleanField(default=True)

    def is_active(self):
        return self.user.is_active

    def __str__(self):
        return self.user.username

    objects = models.Manager()
    active = ActiveImagerManager()

    def followers(self):
        '''List all users followers'''
        return ImagerProfile.objects.filter(following__exact=self)

    def following_list(self):
        '''List of all profiles user is following'''
        return self.following.all()

    def follow(self, user_prof):
        '''Create following relationship between profiles, can't add self'''
        if self not in user_prof.blocking.all():
            self.following.add(user_prof)

    def unfollow(self, user_prof):
        '''Remove following relationship between profiles'''
        self.following.remove(user_prof)

    def block(self, user_prof):
        '''Create blocking realtionship'''
        self.blocking.add(user_prof)

    def unblock(self, user_prof):
        '''Unblock user relationship'''
        self.blocking.remove(user_prof)

    def create_thumbnail(self):
        '''Creates Thumbnail of images'''
        if not self.picture:
            return
        THUMBNAIL_SIZE = (200, 200)
        DJANGO_TYPE = self.picture.file.content_type

        if DJANGO_TYPE == 'image/jpeg':
            PIL_TYPE = 'jpeg'
            FILE_EXTENSION = 'jpg'
        elif DJANGO_TYPE == 'image/png':
            PIL_TYPE = 'png'
            FILE_EXTENSION = 'png'

        image = Image.open(StringIO(self.image.read()))
        # Image.ANITALIAS makes the image look better, preventing artifacts.
        image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

        temp_handle = StringIO()
        image.save(temp_handle, PIL_TYPE)
        temp_handle.seek(0)

        suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
                                 temp_handle.read(), content_type=DJANGO_TYPE)

        self.thumbnail.save('%s_thumbnail.%s'%(os.path.splitext(suf.name)[0],FILE_EXTENSION), suf, save=False)

    def save(self):
        self.create_thumbnail()

        super(ImagerProfile, self).save()

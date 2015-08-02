from imager_images.models import Photo, Album
from django.contrib.auth.models import User
from django.test import TestCase
import factory
import datetime
from django.test.utils import override_settings


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)
    username = 'elenore'


class PhotoFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Photo
    # picture = factory.LazyAttribute(lambda a: File(open('photos/example.jpg')))
    picture = factory.django.ImageField()
    title = 'image1'
    description = 'a photo'


class AlbumFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Album
    title = 'album1'
    description = 'an album'


@override_settings(MEDIA_ROOT='/tmp/django-imager/')
class TestPhoto(TestCase):
    def setUp(self):
        self.elenore = UserFactory()
        self.onephoto = PhotoFactory.create(user=self.elenore)
        self.twophoto = PhotoFactory.create(user=self.elenore, PUBLISHED='shared')
        self.threephoto = PhotoFactory.create(user=self.elenore, PUBLISHED='public')

    def test_picture(self):
        assert self.onephoto.picture.name.startswith('photos/example')

    def test_user(self):
        assert self.onephoto.user == self.elenore

    def test_title(self):
        '''Assert that picture contains a title'''
        self.assertEqual(self.onephoto.title, 'image1')

    def test_description(self):
        '''Assert picture contains description'''
        self.assertEqual(self.onephoto.description, 'a photo')

    def test_date_uploaded(self):
        '''Assert photo has upload date'''
        assert self.onephoto.date_uploaded == datetime.date.today()

    def test_date_modified(self):
        '''Assert Photo has modified date'''
        assert self.onephoto.date_modified == datetime.date.today()

    def test_date_published(self):
        '''Assert Photo has published date or null'''
        assert self.onephoto.date_published is None

    def test_private(self):
        '''Assert default privacy option is private; no one can view'''
        self.assertEqual(self.onephoto.PUBLISHED, 'private')

    def test_shared(self):
        '''Assert option for shared; friends can view'''
        assert self.twophoto.PUBLISHED == 'shared'

    def test_public(self):
        '''Assert option for public; anyone can view that follows'''
        assert self.threephoto.PUBLISHED == 'public'


@override_settings(MEDIA_ROOT='/tmp/django-imager/')
class TestAlbum(TestCase):
    def setUp(self):
        self.elenore = UserFactory.create()
        self.rigby = UserFactory.create()
        self.onephoto = PhotoFactory.create(user=self.elenore)
        self.onealbum = AlbumFactory.create(user=self.elenore)
        self.twophoto = PhotoFactory.create(user=self.rigby)

    def test_user(self):
        assert self.onealbum.user == self.elenore

    def test_pictures(self):
        self.onealbum.pictures.add(self.onephoto)
        assert self.onephoto in self.onealbum.pictures.all()

    def test_pictures_wrong_user(self):
        self.onealbum.pictures.add(self.twophoto)
        print self.onealbum.pictures.all()

    def test_title(self):
        '''Assert that album contains a title'''
        self.assertEqual(self.onealbum.title, 'album1')

    def test_description(self):
        '''Assert album contains description'''
        self.assertEqual(self.onealbum.description, 'an album')

    def test_date_created(self):
        '''Assert album has upload date'''
        assert self.onealbum.date_created == datetime.date.today()

    def test_date_modified(self):
        '''Assert album has modified date'''
        assert self.onealbum.date_modified == datetime.date.today()

    def test_date_published(self):
        '''Assert photo has published date or null'''
        assert self.onealbum.date_published is None

    def test_private(self):
        '''Assert default privacy option is private; no one can view'''
        assert self.onealbum.PUBLISHED == 'private'

    def test_shared(self):
        '''Assert option for shared; friends can view'''

    def test_public(self):
        '''Assert option for public; anyone can view that follows'''

    def test_cover(self):
        '''Assert one contained photo as cover for album'''
        self.onealbum.pictures.add(self.onephoto)
        self.onealbum.designate_cover(self.onephoto)
        self.assertEqual(self.onealbum.cover, self.onephoto)

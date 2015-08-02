from imager_images.models import Photo, Album
from django.contrib.auth.models import User
from django.test import TestCase
from django.core.files import File
import factory
import datetime


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)
    username = 'elenore'


class PhotoFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Photo
    picture = factory.LazyAttribute(lambda a: File(open('photos/example.jpg')))
    # picture = factory.django.ImageField()
    title = 'image1'
    description = 'a photo'


class AlbumFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Album
    title = 'album1'
    description = 'an album'


class TestPhoto(TestCase):
    def setUp(self):
        self.elenore = UserFactory.create()
        self.rigby = UserFactory.create(username='rigby')
        self.elenorephoto = PhotoFactory.create(user=self.elenore)
        self.rigbyphoto = PhotoFactory.create(user=self.rigby)

    def test_photo_belongs_to_unique_user(self):
        assert self.elenorephoto.user == self.elenore
        assert self.elenorephoto in self.elenore.photo.all()


class TestAlbum(TestCase):
    def setUp(self):
        self.elenore = UserFactory.create()
        self.rigby = UserFactory.create(username='rigby')
        self.elenorephoto = PhotoFactory.create(user=self.elenore)
        self.rigbyphoto = PhotoFactory.create(user=self.rigby)
        self.rigbyalbum = AlbumFactory.create(user=self.rigby)
        self.elenorealbum = AlbumFactory.create(user=self.elenore)

    def test_user_album(self):
        '''Assert album contains only user's photos'''
        self.assertEqual(self.elenorealbum.user.username, 'elenore')
        self.assertEqual(self.rigbyalbum.user.username, 'rigby')

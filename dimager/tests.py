from dimager.models import ImagerProfile
from dimager.models import Photo, Albums
from django.contrib.auth.models import User
from django.test import TestCase
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)
    username = 'elenore'


class PhotoFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Photo

    profile = UserFactory.create(username='elenore').ImagerProfile


class AlbumFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Albums

    user = UserFactory.create(username='Freddy')


class TestCaseImagerProfile(TestCase):
    def setup(self):
        self.test_user = UserFactory.create()

    def test_create_profile(self):
        '''Test that every user gets a profile'''
        assert self.test_user.profile

    def test_delete_profile(self):
        '''Test that profile deleted from database'''
        self.test_user.delete()
        assert len(ImagerProfile.objects.all()) == 0

    def test_is_active(self):
        '''Test that user is active user'''
        assert self.test_user.profile.is_active()


class TestCaseFollowBlock(TestCase):
    def setup(self):
        self.elenore = UserFactory()
        self.rigby = UserFactory(username='rigby')

    def test_followers(self):
        '''Test for follower relationship'''
        self.elenore.profile.follow(self.rigby.profile)
        self.assertIn(self.elenore.profile, self.rigby.profile.followers())

    def test_following_list(self):
        '''Test for following relationship'''
        self.elenore.profile.follow(self.rigby.profile)
        self.assertIn(self.rigby.profile, self.elenore.profile.following_list())

    def test_follow(self):
        '''Test for ability to follow'''
        self.elenore.profile.follow(self.rigby.profile)
        self.assertIn(self.rigby.profile, self.elenore.profile.following.all())

    def test_unfollow(self):
        '''Test for ability to unfollow'''
        self.elenore.profile.follow(self.rigby.profile)
        self.elenore.profile.unfollow(self.rigby.profile)
        self.assertNotIn(self.rigby.profile, self.elenore.profile.following_list())

    def test_block(self):
        self.elenore.profile.follow(self.rigby.profile)
        self.rigby.profile.block(self.elenore.profile)
        self.assertIn(self.elenore.profile, self.rigby.profile.blocking.all())

    def test_unblock(self):
        '''Test ability to unblock user profile'''
        self.elenore.profile.follow(self.rigby.profile)
        self.rigby.profile.block(self.elenore.profile)
        self.assertIn(self.elenore.profile, self.rigby.profile.blocking.all())
        self.rigby.profile.unblock(self.elenore.profile)
        self.assertNotIn(self.elenore.profile, self.rigby.profile.blocking.all())


class TestPhoto(TestCase):
    def setup(self):
        self.elenor = UserFactory.create()
        self.rigby = UserFactory.create(username='rigby')
        self.elenorphoto = PhotoFactory.create(profile=self.elenor.ImagerProfile)
        self.rigbyphoto = PhotoFactory.create(profile=self.rigby.ImagerProfile)

    def test_photo_belongs_to_unique_user(self):
        self.assertEqual(str(self.elenorphoto.profile), 'Elenor')

    def test_title(self):
        '''Assert that picture contains a title'''
        self.assertEqual(self.bobphoto.title, 'No Title')

    def test_description(self):
        '''Assert picture contains description'''
        self.assertEqual(self.bobphoto.description, 'No Description')

    # def test_date_uploaded(self):
    #     '''Assert photo has upload date or null'''
    #     assert Photo.date_uploaded == now()

    # def test_date_modified(self):
    #     '''Assert Photo has modified date or null'''
    #     assert Photo.date_modified == now()

    # def test_date_published(self):
    #     '''Assert Photo has published date or null'''
    #     assert Photo.date_published == today()

    def test_private(self):
        '''Assert default privacy option is private; no one can view'''
        self.assertEqual(self.bobphoto.published, 'private')

    def test_shared(self):
        '''Assert option for shared; friends can view'''

    def test_public(self):
        '''Assert option for public; anyone can view that follows'''


class TestAlbum(TestCase):
    def setup(self):
        self.elenor = UserFactory.create()
        self.rigby = UserFactory.create(username='rigby')
        self.elenorphoto = PhotoFactory.create(profile=self.elenor.ImagerProfile)
        self.rigbyphoto = PhotoFactory.create(profile=self.rigby.ImagerProfile)
        self.rigbyalbum = AlbumFactory.create(user=self.rigby)
        self.elenoralbum2 = AlbumFactory.create(user=self.elenor)

    def test_user_album(self):
        '''Assert album contains only user's photos'''
        self.assertEqual(self.elenoralbum.user.username, 'elenor')
        self.assertEqual(self.rigbyalbum.user.username, 'rigby')

    def test_title(self):
        '''Assert that album contains a title'''
        self.assertEqual(self.rigbyalbum.title, 'No Title')

    def test_description(self):
        '''Assert album contains description'''
        self.assertEqual(self.rigbyalbum.description, 'No description')

    def test_date_uploaded(self):
        '''Assert album has upload date or null'''

    def test_date_modified(self):
        '''Assert album has modified date or null'''

    def test_date_published(self):
        '''Assert photo has published date or null'''

    def test_private(self):
        '''Assert default privacy option is private; no one can view'''

    def test_shared(self):
        '''Assert option for shared; friends can view'''

    def test_public(self):
        '''Assert option for public; anyone can view that follows'''

    def test_cover(self):
        '''Assert one contained photo as cover for album'''
        self.rigbyalbum.designate_cover(self.rigbyphoto)
        self.assertEqual(self.rigbyalbum.cover, self.rigbyphoto.photo)

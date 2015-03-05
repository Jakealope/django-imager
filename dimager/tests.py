from django.test import TestCase
from django.contrib.auth.models import User
from dimager.models import ImagerProfile
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)
    username = 'elenore'


class TestCase_ImagerProfile(TestCase):
    def setUp(self):
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


class TestCase_FollowBlock(TestCase):
    def setUp(self):
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

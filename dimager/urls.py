from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from imagerprofile.views import (ImagerProfileUpdateView, profile,
                                 user_profile, library, stream,
                                 photo_form, album_form)

urlpatterns = patterns('',
                       url(r'^$', profile, name='my_profile'),
                       url(r'^photo/add$', photo_form, name='photo_form'),
                       url(r'^album/add$', album_form, name='album_form'),
                       url(r'^library/$', library, name='library'),
                       # url(r'^stream/$', stream, name='stream'),
                       url(r'^(?P<id>\d+)/$', user_profile, name='profile'),
                       url(r'^(?P<pk>\d+)/edit/$',
                           login_required(ImagerProfileUpdateView.as_view()),
                           name='profile_edit'),
                       )

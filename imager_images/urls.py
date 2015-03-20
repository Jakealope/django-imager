from django.conf.urls import patterns, url
from views import AddPhoto, AddAlbum
from django.contrib.auth.decorators import login_required
from imager_images.views import PhotoEditUpdateView, AlbumEditUpdateView


urlpatterns = patterns(
    '',
    url(r'^photo/add/$',
        login_required(AddPhoto.as_view()),
        name='photo_add'),
    url(r'^album/add/$',
        login_required(AddAlbum.as_view()),
        name='album_add'),
    url(r'^photo/edit/(?P<pk>\d+)/$',
        login_required(PhotoEditUpdateView.as_view()),
        name='photo_edit'),
    url(r'^album/edit/(?P<pk>\d+)/$',
        AlbumEditUpdateView.as_view(),
        name='album_edit'),
)

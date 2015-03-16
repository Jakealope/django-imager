from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from django.shortcuts import render
from imager_images.models import Photo, Album, User


def stub(request, *args, **kwargs):
    body = 'Stub View\n\n'
    if args:
        body += 'Args:\n'
        body += '\n'.join(['\t%s' % a for a in args])
    if kwargs:
        body += 'Kwargs:\n'
        body += '\n'.join(['\t%s: %s' % i for i in kwargs.items()])
    return HttpResponse(body, content_type='text/plain')


def home(request):
    context = {'name': 'bob'}
    return render(request, 'home.html', context)
    try:
        random_photo = Photo.random_photo.all()[0]
    except:
        random_photo = None
    return render(request, 'home.html', {
        'random_photo': random_photo
    })


def library(request, id):
    user = User.objects.get(pk=id)
    try:
        albums = Album.objects.filter(user=user).all()
    except:
        albums = None
    try:
        photos = Photo.objects.filter(user=user).all()
    except:
        photos = None
    return render(request, 'library.html', {
        'user': user,
        'albums': albums,
        'photos': photos
    })


def stream(request, id):
    # import pdb; pdb.set_trace()
    user = User.objects.get(pk=id)
    try:
        my_albums = request.user.albums.filter(user=user).all()
    except:
        my_albums = None
    try:
        followed_albums = Album.objects.filter(user=user.profile.is_following()).all()
    except:
        followed_albums = None
    try:
        photos = Photo.objects.filter(user=user).all()
    except:
        photos = None
    try:
        followed_photos = Photo.objects.filter(user=user.profile.is_following()).all()
    except:
        followed_photos = None
    return render(request, 'stream.html', {
        'user': user,
        'my_albums': my_albums.order_by('-date_created'),
        'followed_albums': followed_albums.order_by('-date_created'),
        'photos': photos.order_by('-date_uploaded'),
        'followed_photos': followed_photos.order_by('-date_uploaded'),
    })

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dimager.models import ImagerProfile
from imager_images.models import Album, Photo, User
from django.views.generic import CreateView, UpdateView, DeleteView


@login_required()
def user_profile(request, id):
    user = User.objects.get(id=id)
    try:
        albums = Album.objects.filter(user=user).all()
    except:
        albums = None
    profile = ImagerProfile.objects.get(user=user)
    num_photos = Photo.objects.filter(user=user).count()
    return render(request, 'profile.html', {
        'albums': albums,
        'user': user,
        'profile': profile,
        'num_photo': num_photos
    })


@login_required()
def user_profile(request):
    user = request.user
    try:
        albums = Album.objects.filter(user=user).all()
    except:
        albums = None
    profile = ImagerProfile.objects.get(user=user)
    num_photos = Photo.objects.filter(user=user).count()
    return render(request, 'profile.html', {
        'albums': albums,
        'user': user,
        'profile': profile,
        'num_photo': num_photos
    })


@login_required()
def library(request):
    user = request.user
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


@login_required()
def stream(request):
    user = request.user
    try:
        albums = Album.objects.filter(user=user).order_by('-date_created')
    except:
        albums = None
    try:
        followed_albums = Album.objects.filter(user=user.
                                               profile.is_following()).order_by('-date_created')
    except:
        followed_albums = None
    try:
        photos = Photo.objects.filter(user=user).order_by('-date_uploaded')
    except:
        photos = None
    try:
        followed_photos = Photo.objects.filter(user=user.
                                               profile.is_following()).order_by('-date_uploaded')
    except:
        followed_photos = None
    return render(request, 'stream.html', {
        'user': user,
        'albums': albums,
        'followed_albums': followed_albums,
        'photos': photos,
        'followed_photos': followed_photos,
    })


class ImagerProfileUpdateView(UpdateView):
    model = ImagerProfile
    template_name_suffix = '_update_form'
    success_url = '/profile/'
    fields = [
        'profile_image',
        'phone_number',
        'birthday',
        'phone_privacy',
        'birthday_privacy',
        'picture_privacy',
        'name_privacy',
        'email_privacy',
        'following',
        'blocking',
    ]

    def get_queryset(self):
        qs = super(ImagerProfileUpdateView, self).get_queryset()
        return qs.filter(user=self.request.user)

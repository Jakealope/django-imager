from django.shortcuts import render
from imager_images.forms import UserForm, ImagerProfileForm
# from media import profile_image
from django.core.urlresolvers import reverse_lazy, reverse
from models import Photo, Album
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect
from dimager.models import ImagerProfile


def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ImagerProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.profile_image = request.FILES
                profile.profile_image = request.FILES['picture']

            profile.save()
            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = ImagerProfileForm()

    return render_to_response(
        'dimager/imager/templates/registration/home.html')


class AddPhoto(CreateView):
    model = Photo
    fields = ['title', 'description', 'picture', 'PUBLISHED']
    template_name = 'photo_add.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPhoto, self).form_valid(form)

    # success_url = reverse_lazy('library')

    def get_success_url(self):
        return reverse('library')

class PhotoEditUpdateView(UpdateView):
    model = Photo
    fields = ['title', 'description', 'PUBLISHED']
    template_name = 'photo_edit.html'

    def dispatch(self, request, *args, **kwargs):
        photo_profile = Photo.objects.get(id=int(self.kwargs['pk'])).profile
        user_profile = ImagerProfile.objects.get(user=self.request.user)
        if photo_profile != user_profile:
            return redirect('/accounts/login/')
        return super(PhotoEditUpdateView, self).dispatch(request, *args, **kwargs)
    # success_url = reverse_lazy('library')

    


class AlbumEditUpdateView(UpdateView):
    model = Photo
    fields = ['title', 'description', 'pictures', 'cover', 'PUBLISHED']
    template_name = 'album_edit.html'

    def dispatch(self, request, *args, **kwargs):
        album_profile = Album.objects.get(id=int(self.kwargs['pk'])).profile
        user_profile = ImagerProfile.objects.get(user=self.request.user)
        if album_profile != user_profile:
            return redirect('/accounts/login/')
        return super(AlbumEditUpdateView, self).dispatch(request, *args, **kwargs)
    success_url = reverse_lazy('library')


class AddAlbum(CreateView):
    model = Album
    fields = ['title', 'description', 'pictures', 'cover', 'PUBLISHED']
    template_name = 'album_add.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddAlbum, self).form_valid(form)

    success_url = reverse_lazy('library')

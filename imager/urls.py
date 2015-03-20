from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy
from imager import views as main_views
from registration.backends.simple.views import RegistrationView
from django.conf import settings


class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return '/profile/'


urlpatterns = patterns(
      '',
      url(r'^$', main_views.home, name='home'),
      # url(r'^blog/', include('blog.urls')),
      url(r'^', include('imager_images.urls')),

      url(r'^accounts/', include('registration.backends.simple.urls')),

      url(r'^admin/', include(admin.site.urls)),

      url(r'^profile/', 'dimager.views.user_profile'),

      url(r'^login/$', auth_views.login,
          {'template_name': 'registration/login.html'}, name='auth_login'),

      url(r'^logout/$', auth_views.logout,
          {'template_name': 'registration/logout.html'}, name='auth_logout'),

      url(r'^password/change/$', auth_views.password_change,
          {'post_change_redirect': reverse_lazy('auth_password_change_done')},
          name='auth_password_change'),

      url(r'^password/change/done/$', auth_views.password_change_done,
          name='auth_password_change_done'),

      url(r'^password/reset/$', auth_views.password_reset,
          {'post_reset_redirect': reverse_lazy('auth_password_reset_done')},
          name='auth_password_reset'),

      url(r'^password/reset/complete/$', auth_views.password_reset_complete,
          name='auth_password_reset_complete'),

      url(r'^password/reset/done/$', auth_views.password_reset_done,
          name='auth_password_reset_done'),

      url(r'^library/', 'dimager.views.library', name='library'),
      url(r'^stream/', 'dimager.views.stream'),

      # url(r'^photo/add', 'imager_images.views.AddPhoto'),

      # url(r'^album/add', 'imager_images.views.AddAlbum'),

       )
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

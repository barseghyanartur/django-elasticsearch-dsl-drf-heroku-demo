from django.conf import settings
from django.conf.urls import include, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView

from search_indexes import urls as search_index_urls

admin.autodiscover()

urlpatterns = [
    # django-admin-timeline URLs. Should come before the django-admin URLs.
    re_path(r'^search/', include(search_index_urls)),

    re_path(r'^admin/', admin.site.urls),

    re_path('^$', RedirectView.as_view(pattern_name='api-root'), name='home')
]

# Serving media and static in debug/developer mode.
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

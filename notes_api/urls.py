from django.contrib import admin
from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from notes import views as notes_views

router = DefaultRouter()
router.register(r'notes', notes_views.NoteViewSet, 'note')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]


urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
]

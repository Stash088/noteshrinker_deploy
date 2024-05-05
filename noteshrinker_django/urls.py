from django.urls import include, path
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from noteshrinker import views as noteshrinker_views

urlpatterns = [
    path(r'admin', admin.site.urls),
    path(r'', include('noteshrinker.urls'))

]
urlpatterns += i18n_patterns(
    path((r''), noteshrinker_views.PictureCreateView.as_view(), name='index'),
)
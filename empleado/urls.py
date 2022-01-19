from django.contrib import admin
from django.urls import path,re_path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('',include('apps.departamento.urls')),
    re_path('',include('apps.home.urls')),
    re_path('',include('apps.persona.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from entrega1_continoemiliano.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include ('app1.urls')),
    path('', include('app1.urls')),
    path('accounts/', include ('accounts.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root= MEDIA_ROOT )


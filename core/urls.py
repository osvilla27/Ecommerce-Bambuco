from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include, re_path

from apps.product.urls import router_product


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.user.urls')),

    path('api/', include(router_product.urls)),
    path('api/', include('apps.product.urls')),
    
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

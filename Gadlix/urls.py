from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Web.urls',namespace="Web")),

    path('tinymce/', include('tinymce.urls')),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "GADLIX Administration"
admin.site.site_title = "GADLIX Admin Portal"
admin.site.index_title = "Welcome to GADLIX Admin Portal"
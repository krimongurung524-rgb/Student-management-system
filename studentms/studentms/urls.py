from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('core.urls')),
    path('', RedirectView.as_view(pattern_name='student_list')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
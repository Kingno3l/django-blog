# from django.contrib import admin
# from django.urls import path, include
# from .import views
# from django.contrib.staticfiles import staticfiles_urlpatterns
# from django.conf.urls.static import static
# from django.conf import settings

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('articles/', include('articles.urls')),
#     path('about/', views.about),
#     path('', views.homepage),
# ]

# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views  # Ensure this imports the views from the correct file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),  # Include articles app URLs
    path('accounts/', include('accounts.urls')),
    path('about/', views.about, name='about'),  # Your 'about' view
    path('', views.homepage, name='homepage'),  # Your homepage view
]

# Serving static files during development
urlpatterns += staticfiles_urlpatterns()

# Serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

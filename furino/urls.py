from django.contrib import admin
from django.views.static import serve
from django.urls import include, path, re_path
from furino import settings
from main import views as general_views

admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/accounts/', include('registration.backends.default.urls')),
    path('',include(('main.urls'),namespace='main')),   
    path('',general_views.app,name='app'), 
    
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
]
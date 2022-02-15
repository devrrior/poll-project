from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from apps.users.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('login/', LoginView.as_view(),name = 'login'),
    path('admin/', admin.site.urls),
    path('logout/', LogoutView.as_view(), name = 'logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

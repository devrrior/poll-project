from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from apps.users.views import LoginView, SignUpView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('polls/', include('apps.polls.urls')),
    path('login/', LoginView.as_view(),name = 'login'),
    path('signup/', SignUpView.as_view(),name = 'signup'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

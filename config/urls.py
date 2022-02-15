from django.contrib import admin
from django.urls import include, path

from apps.users.views import LoginView

urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('login/', LoginView.as_view(),name = 'login'),
    path('admin/', admin.site.urls),
]

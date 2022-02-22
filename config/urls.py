from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from apps.user.views import LoginView, SignUpView
from django.contrib.auth.views import LogoutView

from apps.vote.views import VotePollView

urlpatterns = [
    path('user/', include('apps.user.urls')),
    path('poll/', include('apps.poll.urls')),
    path('question/', include('apps.question.urls')),
    path('vote', VotePollView.as_view(), name='vote'),
    path('login/', LoginView.as_view(),name = 'login'),
    path('signup/', SignUpView.as_view(),name = 'signup'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

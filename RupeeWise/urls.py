from django.contrib import admin
from django.urls import path
from user_auth import views as user_view
from user_expense import views as expense_view
from user_profile import views as profile_view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_view.register, name = 'register'),
    path('login/', user_view.login, name = 'login'),
    path('logout/', user_view.logout, name = 'logout'),
    path('dashboard/', expense_view.dashboard, name = 'dashboard'),
    path('profile/', profile_view.profile, name = 'profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('contents.urls')),
                  path('accounts/', include('accounts.urls')),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('', include('friendship.urls')),
                  path('', include('chats.urls'))
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

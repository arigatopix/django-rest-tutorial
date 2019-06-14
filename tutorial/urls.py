from django.contrib import admin
from django.urls import path, include

# ! ไม่ต้อง import urls ของ app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quickstart.urls')),
    path('snippets/', include('snippets.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

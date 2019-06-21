from django.contrib import admin
from django.urls import path, include

# ! ไม่ต้อง import urls ของ app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quickstart.urls')),
    path('', include('snippets.urls')),
]

# เพิ่ม Login Button มุมบนขวา ใช้ += ไม่ว่าจะไปหน้าไหนก็จะมีปุ่ม login
# จะเพิ่ม urls /users/ อัตโนมัติ
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
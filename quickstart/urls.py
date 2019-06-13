from django.urls import include, path
from rest_framework import routers
from quickstart import views

# registering the viewsets with router class
router = routers.DefaultRouter()
""" จะใช้ routers ได้ต้องเป็น viewsets """
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing เอา routers มาเชื่อมกับ ''/..
# Additionally, we include login URLs for the browsable API. (login and logout view use browsable API)
urlpatterns = [
  path('', include(router.urls)),
]

from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from snippets import views

# ใช้ DefaultRouter เพื่อ Bind และคิดให้อัตโนมัติว่า pattern จะเป็นยังไง ???

# Create a router and register our viewsets with it.
# แค่ register viewset ตัว Rest จะทำให้กำหนด method และ url ให้
# custom ได้ เช่น
# path('snippets/<int:pk>/custom/', views.SnippetViewSet.as_view({ 'get' : 'retrieve'}), name='snippet-highlight'),
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

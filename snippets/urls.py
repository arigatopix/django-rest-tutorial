from django.urls import path
# set format สำหรับแสดงผล
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
""" ตั้งค่าให้แสดงผล รับค่าได้ทุก format (เสริม request.data ที่สามารถรับ data ได้ทุก format) """
from django.urls import path
# set format สำหรับแสดงผล
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    # path('', views.api_root),
    path('snippets/',
        views.SnippetList.as_view(),
        name='snippet-list'),
    path('snippets/<int:pk>',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),
    path('snippets/<int:pk>/highlight/',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    path('users/',
        views.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>',
        views.UserDetail.as_view(),
        name='user-detail'),
]

""" 
- ใช้ Hyperlinked API ต้องใส่ชื่อ name เพื่อระบุว่า url จะเรียก class view อันไหน  
    - root API ใช้ {models}-list
    - Serializer API ใช้ {models}-{field}
    - url อื่นๆ API ใช้ {models}-detail
"""


urlpatterns = format_suffix_patterns(urlpatterns)
""" ตั้งค่าให้แสดงผล รับค่าได้ทุก format (เสริม request.data ที่สามารถรับ data ได้ทุก format) """
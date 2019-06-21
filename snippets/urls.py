from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import SnippetViewSet, UserViewSet

# กำหนด set of views ของ ViewSets และเอาไปใส่ใน path url (ในส่วนของ view) จะทำ method ใดได้บ้าง
# creating multiple views from each ViewSet class, binding the http methods
snippet_list = SnippetViewSet.as_view({
    'get' : 'list',
    'post' : 'create'
})

snippet_detail = SnippetViewSet.as_view({
    'get' : 'retrieve',
    'post' : 'create',
    'patch' : 'partial_update',
    'delete' : 'destroy',
})

snippet_highlight = SnippetViewSet.as_view({
    'get' : 'highlight',
})

user_list = UserViewSet.as_view({
    'get' : 'list'
})

user_detail = UserViewSet.as_view({
    'get' : 'retrieve'
})


urlpatterns = [
    path('snippets/',
        snippet_list,
        name='snippet-list'),
    path('snippets/<int:pk>',
        snippet_detail,
        name='snippet-detail'),
    path('snippets/<int:pk>/highlight/',
        snippet_highlight,
        name='snippet-highlight'),
    path('users/',
        user_list,
        name='user-list'),
    path('users/<int:pk>',
        user_detail,
        name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

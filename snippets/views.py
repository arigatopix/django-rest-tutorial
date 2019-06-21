from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, renderers
from rest_framework.response import Response
from rest_framework.decorators import action
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from snippets.permissions import IsOwnerOrReadOnly


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `detail`, `retrieve`, `update`, `destroy` actions
    * ต้องไป set ใน url ว่าแต่ละ ViewSets จะใช้กับ method ใดได้บ้าง
    """
    
    queryset = Snippet.objects.all()
    """ เรียก object ใน models """
    serializer_class = SnippetSerializer
    """ queryset และ serializer_class จะเป็น logic ในการ get, post และ save ลง db"""
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )
    
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        """ เป็น field ที่สั่งให้ render Html (สร้าง html ตาม models) """
        snippet = self.get_object()
        return Response(snippet.highlighted)
        """ Mark viewset routable method actions (เช่น get, post) และ add custom method รวมถึงสั่ง route url ได้"""

    # เปลี่ยนรูปแบบ behaviour ของ serializers
    def perform_create(self, serializer):
        """ overide ในส่วนของ field ที่เพิ่มเข้ามาว่าใช้ข้อมูลจาก user """
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    * This viewset automatically provides `list` and `detail` actions.
    * User ให้ read only
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

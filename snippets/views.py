from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins, generics
"""
- use mixins build block ของ generics ทำหน้าที่ list, create, retrieve, update, destroy logic
- generics คือรวบรวม beheviour (list, create, retrieve, update, destroy ของ mixins ไว้แล้ว) เกี่ยวกับ views แสดงผลใน web มี form ให้กรอกด้วย 
- จะช่วยลดการเขียน code เพราะว่า django_rest จะรวม behaviour ที่ backend ใช้บ่อยๆ รวมไปในตัวเลย  เพราะ django รู้ว่าเราจะทำงาน create/retrieve/update/delete operations กับ model เสมอ
- ลดการเขียน status, Response, APIView
"""


class SnippetList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    """ list and create """
    
    queryset = Snippet.objects.all()
    """ เรียก object ใน models """
    serializer_class = SnippetSerializer
    """
    django_restframework จะเอา serializer_class ไปคิดตาม logic
        - get จะเรียก queryset ไปแสดง
        - post จะเช็ค request รับเข้า แล้วก็เช็ค valid เป็นต้น
    """

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    
class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """ 
    Retrieve คือการ get แบบมี id (รายการเดียว), update or delete a snippet instance.
    - genericAPIView จะ provide function .retrieve(), update() .destroy() แสดงเป็น view
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
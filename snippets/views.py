from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics
"""
- use mixins build block ของ generics ทำหน้าที่ list, create, retrieve, update, destroy logic
- generics คือรวบรวม beheviour (list, create, retrieve, update, destroy ของ mixins ไว้แล้ว) เกี่ยวกับ views แสดงผลใน web มี form ให้กรอกด้วย 
- จะช่วยลดการเขียน code เพราะว่า django_rest จะรวม behaviour ที่ backend ใช้บ่อยๆ รวมไปในตัวเลย  เพราะ django รู้ว่าเราจะทำงาน create/retrieve/update/delete operations กับ model เสมอ
- ลดการเขียน status, Response, APIView
"""


class SnippetList(generics.ListCreateAPIView):
    """ list and create แบบไม่ใช้ mixins """
    
    queryset = Snippet.objects.all()
    """ เรียก object ใน models """
    serializer_class = SnippetSerializer
    """
    django_restframework จะเอา serializer_class ไปคิดตาม logic
        - get จะเรียก queryset ไปแสดง
        - post จะเช็ค request รับเข้า แล้วก็เช็ค valid เป็นต้น
    """


    
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """ 
    - genericAPIView จะ provide function .retrieve(), update() .destroy() แสดงเป็น view
    - ใช้ generics ในการ Retrieve, update, destroy รวมเป็นอันเดียวเลย generics.RetrieveUpdateDestroyAPIView
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
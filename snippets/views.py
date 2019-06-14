from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
""" permissions แบ่งแยกคนที่ login หรือไม่ login สามารถทำอะไรได้บ้าง """
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from snippets.permissions import IsOwnerOrReadOnly
"""
- use mixins build block ของ generics ทำหน้าที่ list, create, retrieve, update, destroy logic
- generics คือรวบรวม beheviour (list, create, retrieve, update, destroy ของ mixins ไว้แล้ว) เกี่ยวกับ views แสดงผลใน web มี form ให้กรอกด้วย 
- จะช่วยลดการเขียน code เพราะว่า django_rest จะรวม behaviour ที่ backend ใช้บ่อยๆ รวมไปในตัวเลย  เพราะ django รู้ว่าเราจะทำงาน create/retrieve/update/delete operations กับ model เสมอ
- ลดการเขียน status, Response, APIView
"""


class SnippetList(generics.ListCreateAPIView):
    """
    list and create แบบไม่ใช้ mixins
    """
    
    queryset = Snippet.objects.all()
    """ เรียก object ใน models """
    serializer_class = SnippetSerializer
    """
    django_restframework จะเอา serializer_class ไปคิดตาม logic
        - get จะเรียก queryset ไปแสดง
        - post จะเช็ค request รับเข้า แล้วก็เช็ค valid เป็นต้น
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )
    
    """ 
     * จำกัดให้คนที่ไม่ได้ login อ่านได้อย่างเดียว
        - เป็น tuple ต้องใส่ , ด้านหลัง
    """

    # เปลี่ยนรูปแบบ behaviour ของ serializers
    def perform_create(self, serializer):
        """ 
         - เนื่องจากว่า serializer รวมกระบวนการ valid, save instance ไว้ด้วยแล้ว แต่กรณีนี้มี field เฉพาะที่ serializer ต้องรับจึงต้องตั้งค่า perform_create()
        - ตั้งค่า perform_create() ใหม่ เพื่อระบุว่า field owner รับข้อมูลมาจาก request.user
        """
        serializer.save(owner=self.request.user)


    
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """ 
    - genericAPIView จะ provide function .retrieve(), update() .destroy() แสดงเป็น view
    - ใช้ generics ในการ Retrieve, update, destroy รวมเป็นอันเดียวเลย generics.RetrieveUpdateDestroyAPIView
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

# UserAPIView จะให้เป็น read-only
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

""" 
กำหนด endpoint ร่วมกับ user models
ป้องกัน beheviour สำหรับการ save
สร้าง permissions เอง และกำหนด permission สำหรับแต่ละ method
กำหนด serializer โดยระบุ user เจ้าของ post
"""
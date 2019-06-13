from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer

# group views เข้าด้วยกัน เพราะแสดงผลเหมือนกัน สามารถใส่ logic organized ง่ายกว่าแยกหลายๆ ไฟล์
# !  ระวังสะกดผิด serializer หรือพวกตัว s
class UserViewSet(viewsets.ModelViewSet):
  """ แสดงผล api โดยใช้ modelViewSet เชื่อมไปหา db Users สามารถ view หรือ edit """
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer
  

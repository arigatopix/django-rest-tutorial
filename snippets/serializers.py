from django.contrib.auth.models import User
from rest_framework import serializers
""" ช่วยสร้าง api (dict) (และรับ request)และเป็น modelForm สามารถทำเป็น json หรือแปลงเป็น django object """
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    """ 
        - ModelSerializer จะ add field model validate ให้เลย ไม่ต้องประกาศ แต่ละ fields แบบละเอียด 
        - imprements from create() and update() method
    """

    owner = serializers.CharField(read_only=True)
    """ ตั้งค่า validate สำหรับ fields owner เพื่อรับค่าจาก api """

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style','owner',)

class UserSerializer(serializers.ModelSerializer):
    """ เอา User models มาทำเป็น serializers และเพิ่ม snippets เข้าไปอีก field นึง
     """
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    """ เพิ่ม relationship ไปใน User models """

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')



"""
+ Dict to JSON
    json = JSONRenderer().render(serializer.data)
+ JSON to Dict (Deserializer) ต้อง import io.BytesIO
    data = JSONParser().parse(json)
+ Form == Serializer เพื่อ get ข้อมูลจาก DB,  ModelForm = ModelSerialzer เพื่อ update, create ค่า เหมือนกันกับ Django
+ Serializers ...
- เอาจาก models มาทำเป็น api มาหน้าที่เป็น form คอย valid ข้อมูลนำเข้า
-- ส่งออก
- แปลงจาก query object ของ django เป็น dict ผ่าน  serializer = SnippetSerializer(snippets, many=True) 
- แปลงจาก dict เป็น json : JsonResponse(serializer.data, safe=False)
-- รับเข้า
data = JSONParser().parse(request)
"""

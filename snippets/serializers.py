from rest_framework import serializers
""" ช่วยสร้าง api (dict) (และรับ request)และเป็น modelForm สามารถทำเป็น json หรือแปลงเป็น django object """
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    """ 
        - ModelSerializer จะ add field model validate ให้เลย ไม่ต้องประกาศ แต่ละ fields แบบละเอียด 
        - imprements from create() and update() method
    """

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style',)


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

from django.contrib.auth.models import User
from rest_framework import serializers
""" ช่วยสร้าง api (dict) (และรับ request)และเป็น modelForm สามารถทำเป็น json หรือแปลงเป็น django object """
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    """ 
        - ModelSerializer จะ add field model validate ให้เลย ไม่ต้องประกาศ แต่ละ fields แบบละเอียด 
        - imprements from create() and update() method
        - HyperlinkedModelSerializer แทน ModelSerializer ทำให้แต่ละ enitities เชื่อมกัน โดยมี link ให้อัตโนมัติ แต่จะไม่มี field id ของ models ให้
        - HyperlinkedIdentifyField คือ class ที่ต้องระบุว่า ให้ link ไปที่ views name อันไหน
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    """ ตั้งค่า validate สำหรับ fields owner เพื่อรับค่าจาก api """
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    """
    * view-name ตั้งชื่อให้ตรงกับ urls ที่สร้าง โดย snippet-hightlight ไปเชื่อมกับ SnippetHighlight
    * ห้ามพิมพ์ผิด !!!
    highlight จะเป็น field URL โดยมี format เป็น html
    """

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner', 'highlight')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ เอา User models มาทำเป็น serializers และเพิ่ม snippets เข้าไปอีก field นึง
     """
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    """ fields สำหรับแสดงรายละเอียดว่า user นี้มี record อะไรบ้าง โดยใช้ HyperlinkedRelatedField จะแสดงผลเป็น url ใน field """


    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')

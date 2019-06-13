from rest_framework import serializers
""" ช่วยสร้าง api (dict) (และรับ request)และเป็น modelForm สามารถทำเป็น json หรือแปลงเป็น django object """
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    """ validate ลอกมาจาก attribute models ได้เลย ยกเว้น created """
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    """ จะบอกว่าเหมือน Form class ของ django ปกติ """
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(
        choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(
        choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        create and return new `Snippet` instance, given the validated data. function สร้าง dict โดยผ่าน class SnippetSerializer
        """
        return Snippet.objects.create(**validated_data)
        # ? validated_data คือ??

    def update(self, instance, validated_data):
        """
        Update and return new `Snippet` instance, given the validated data. 
        """
        # ? คล้ายๆ ว่ารับค่าผ่าน instance แล้วไป validate กับ serializers ก่อน (instance.title ไป validate กับ field 'title') แล้วค่อบเก็บค่า instance.save()
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)

        instance.save()
        """ modified ใน models เมื่อ save """

        return instance


"""
+ Dict to JSON
    json = JSONRenderer().render(serializer.data)
+ JSON to Dict (Deserializer) ต้อง import io.BytesIO
    data = JSONParser().parse(json)
+ Form == Serializer เพื่อ get ข้อมูลจาก DB,  ModelForm = ModelSerialzer เพื่อ update, create ค่า เหมือนกันกับ Django
"""

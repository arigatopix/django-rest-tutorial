# แสดง STATUS CODE พร้อมกับข้อความเช่น HTTP_400_BAD_REQUEST
from rest_framework import status
# api_view ใช้ function based view, APIView ใช้ class based (มี viewset ด้วย ช่วยเพิ่ม logic)
from rest_framework.decorators import api_view
# ช่วย render response ตามที่ client request มา
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


""" อนุญาตให้ GET, POST ในหน้านี้ """
@api_view(['GET','POST'])
def snippet_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == 'GET':
        snippets = Snippet.objects.all()
        """ ดึงข้อมูลจาก model เป็น query object """
        serializer = SnippetSerializer(snippets, many=True)
        """ แปลง query object เป็น dictionary """

        return Response(serializer.data)
        """ Response แทน JsonResponse ได้เลย ส่งค่า JSON """

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        """ 
        - บรรทัดนี้บอกว่าเอาข้อมูลจาก request ไป Serializer
        - request.data จะ Handles data. Work for POST, PUT, DELETE
        """

        if serializer.is_valid():
            """ จะตอบกลับมาเป็น True ถ้าทุก fields เป็นไปตามเงื่อนไขของ Serializer """
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            """ status เปลี่ยนให้ชัดเจนมากขึ้นโดยใช้ method ของ rest_framework """

        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        """ ถ้า invalid ส่งค่า error กับ 400 Bad Request """


""" อนุญาตให้ GET, PUT, DELETE """
@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    """
    - Retrieve, update or delete a code snippet. คือต้องระบุ pk เพื่อ update, delete
     - format ช่วยระบุ format ใน url เช่น snippents/1.json โดย format = ['api',] หรือ ใส่ None ก็จะไม่ระบุว่าจะเป็น format อะไร
        - สามารถ post , get ด้วย Content-type Header แบบไหน เช่น application/json หรือ http/text
        - ต้องไป register ใน url format_suffix_patterns
        - ตัวอย่าง http://127.0.0.1:8000/snippets/1.json
    """
    # for
    try:
        snippet = Snippet.objects.get(pk=pk)
        """ เรียก object ตาม id """
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        """ ดึงจาก model เป็น dict """
        return Response(serializer.data)
        """ แปลงเป็น JSON """

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        """
        - รับค่าจาก client
        - check ค่าที่รับมา validated_data กับ  SnippetSerializer
        """

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

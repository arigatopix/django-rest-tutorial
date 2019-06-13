# แสดง STATUS CODE พร้อมกับข้อความเช่น HTTP_400_BAD_REQUEST
from rest_framework import status
# api_view ใช้ function based view, APIView ใช้ class based (มี viewset ด้วย ช่วยเพิ่ม logic)
from rest_framework.decorators import api_view
# ช่วย render response ตามที่ client request มา
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


# @csrf_exempt
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """

#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         """ ดึงข้อมูลจาก model เป็น query object """
#         serializer = SnippetSerializer(snippets, many=True)
#         """ แปลง query object เป็น dictionary """

#         return JsonResponse(serializer.data, safe=False)
#         """ แสดงผลเป็น JSON format , safe=False คือยอมให้แสดงผล format ที่ไม่ใช่ dict """

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         """ แปลงเป็น dict """
#         serializer = SnippetSerializer(data=data)
#         """ เอา dict ไป valid คล้ายๆ ModelForm data ที่เข้าไปเช็คใน Serializer ทีละ fields """

#         if serializer.is_valid():
#             """ จะตอบกลับมาเป็น True ถ้าทุก fields เป็นไปตามเงื่อนไขของ Serializer """
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#             """ status code 201 คือ create """

#         return JsonResponse(serializer.error, status=400)
#         """ ถ้า invalid ส่งค่า error กับ 400 Bad Request """


# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet. คือต้องระบุ pk เพื่อ update, delete
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#         """ เรียก object ตาม id """
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         """ แสดงผลเป็น json """
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         """ รับค่าจาก client """
#         serializer = SnippetSerializer(snippet, data=data)
#         """ check ค่าที่รับมา validated_data กับ  SnippetSerializer"""

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)

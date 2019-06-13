from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer


@csrf_exempt
def snippet_list(request):
    """ 
    List all code snippets, or create a new snippet.
    """

    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
        """ แสดงผลเป็น JSON format , safe=False คือยอมให้แสดงผล format ที่ไม่ใช่ dict """

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        """ แปลงเป็น dict เก็บลง db """
        serializer = SnippetSerializer(data=data)

        if serializer.is_valid():
            """ ก่อน save ต้อง valid กับ SnippetSerializers ก่อน """
            serializer.save()
            return JsonResponse(serializer.data, status=201)
            """ status code 201 คือ create """

        return JsonResponse(serializer.error, status=400)
        """ ถ้า invalid ส่งค่า error กับ 400 Bad Request """


@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet. คือต้องระบุ pk เพื่อ update, delete
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
        """ เรียก object ตาม id """
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        """ แสดงผลเป็น json """
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        """ รับค่าจาก client """
        serializer = SnippetSerializer(snippet, data=data)
        """ check ค่าที่รับมา validated_data กับ  SnippetSerializer"""

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

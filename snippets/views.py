from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
# แสดง STATUS CODE พร้อมกับข้อความเช่น HTTP_400_BAD_REQUEST
from rest_framework import status
# Class-based view ช่วยให้สร้าง function ที่สามารถ reuse ได้ ต้องไปแก้ใน url ให้มองเป็น class based view ด้วย
from rest_framework.views import APIView
# ช่วย render response ตามที่ client request มา
from rest_framework.response import Response


class SnippetList(APIView):
    """
    List all code snippets, or create a new snippet Use class-based view.
    """

    def get(self, request, format=None):
        """ คล้ายๆ เดิม ไม่ต้องเช็ค request.method """
        snippets = Snippet.objects.all()
        """ retrieve data from models """
        serializer = SnippetSerializer(snippets, many=True)
        """ object to dict """
        return Response(serializer.data)
    
    def post(self, request, formant=None):
        serializer = SnippetSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

class SnippetDetail(APIView):
    """ 
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        """ ทดลอง get ตาม primary key ที่ request มา """
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoseNotExist:
            """ ไม่พบ ส่ง page 404 """
            raise Http404
    
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        """ รับ request และเรียก function get_object ด้านบน เอา object มา"""
        serializer = SnippetSerializer(snippet)
        """ แปลงจาก object เป็น dict. """

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        """ replace snippet ของเดิมด้วย request.data """
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
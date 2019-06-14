from rest_framework import permissions
""" add custom permission """

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    - รับ serializer object และรับ user มา แล้วเข้า class IsOwnerOrReadOnly ไป request.user
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request

        # so we'll always allow GET, HEAD, or OPTIONS requests. (method ดู)
        if request.method in permissions.SAFE_METHODS:
            """ ถ้า method เป็น SAFE_METHODS (get กับ head, option) จะ return True สามารถดูได้"""
            return True

        # Write permissions are only allowed to the owner of the snippet.
        # method ที่สามารถที่ทำได้ทุกอย่าง
        return obj.owner == request.user

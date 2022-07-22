from rest_framework.permissions import BasePermission
from rest_framework.views import Request

from users.models import User


class UserPermission(BasePermission):
    def has_permission(self, request, _):
        staff_methods = {"GET"}
        
        if request.method in staff_methods:
            return request.user.is_superuser
        
        return True
    
class IsAdminOrUser(BasePermission):
    def has_object_permission(self, request: Request, _, obj: User):
        if request.user.is_superuser:
            return True

        return obj == request.user

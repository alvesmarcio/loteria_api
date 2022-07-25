from rest_framework.permissions import BasePermission


class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class ListOrAdminCreatePermission(BasePermission):
    def has_permission(self, request, view):
        admin_methods = ["POST"]
        if request.method in admin_methods:
            return request.user.is_superuser

        return True

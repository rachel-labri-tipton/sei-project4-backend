from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    message = 'You have to be the author in order to change this article.'

    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user


class IsStaffWriter(permissions.BasePermission):
    message = 'You must write for us in order to change this content.'

    def has_object_permissions(self, request, view, obj):
        return request.user.is_staff_writer

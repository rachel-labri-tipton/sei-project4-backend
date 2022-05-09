from rest_framework import permissions


class IsLoggedInUser(permissions.BasePermission):

    def has_object_permissions(self, request, view, obj):
        message = 'You are not allowed to update this profile.'

        return obj.username == request.username


class IsStaffWriter(permissions.BasePermission):
    message = 'You must write for us in order to change this content.'

    def has_object_permissions(self, request, view, obj):
        return request.user.is_staff_writer

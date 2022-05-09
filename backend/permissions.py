from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    message = 'You have to be the author of this blogpost to update it.'

    def has_object_permissins(self, request, view, obj):

        return obj.author == request.user


class IsLoggedInUser(permissions.BasePermission):
    message = 'You are not allowed to update this profile.'

    def has_object_permissions(self, request, view, obj):
        print("user", request.user)
        return obj.username == request.user.username


class IsStaffWriter(permissions.BasePermission):

    def has_object_permissions(self, request, view, obj):
        return request.user.is_staff_writer

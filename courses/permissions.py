from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):

    def has_permission(self, request, view):
        if request.method in ["DELETE", "POST"]:
            return False

        return bool(request.user.groups.filter(name="Moderator"))


class IsStudent(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in ["DELETE", "POST"]:
            return False

        return request.user in obj.students.all()

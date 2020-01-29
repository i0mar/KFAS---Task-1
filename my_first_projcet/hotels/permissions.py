from rest_framework.permissions import BasePermission

class IsBorrower(BasePermission) :
    message = "You can not return a book you have not borrowed"

    def has_object_permission(self, request, view, obj):
        if (request.user == obj.user):
            return True
        else:
            return False


class HasAddedBook(BasePermission) :
    message = "You can not delete a book you have not added"

    def has_object_permission(self, request, view, obj):
        if (request.user == obj.added_by):
            return True
        else:
            return False
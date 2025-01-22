from rest_framework import permissions


class IsAdminOrReadOnly(permissions.IsAdminUser):
    """
    Custom permission class that allows read-write access for admin users
    and read-only access for non-admin users.
    """

    def has_permission(self, request, view):
        """
        Override the `has_permission` method to enforce permissions.

        Admin users are granted full access, while non-admin users
        are restricted to safe (read-only) methods.
        """
        # Check if the user has admin privileges
        is_admin = super().has_permission(request, view)
        # Allow read-only access for non-admin users (safe methods only)
        return is_admin or request.method in permissions.SAFE_METHODS


class IsReviewAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission class that allows read-write access
    only to the author of a review. Other users are limited
    to read-only access.
    """

    def has_object_permission(self, request, view, obj):
        """
        Override the `has_object_permission` method to enforce object-level permissions.

        Safe methods (GET, HEAD, OPTIONS) are allowed for all users,
        while write operations (e.g., PUT, PATCH, DELETE) are restricted
        to the author of the review.
        """
        # Allow safe methods for any user
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow write permissions only for the review's author
        return obj.review_author == request.user

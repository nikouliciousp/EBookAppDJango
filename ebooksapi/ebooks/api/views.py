from django.shortcuts import get_object_or_404
from ebooks.models import Ebook, Review
from rest_framework import generics
from rest_framework.exceptions import ValidationError

from .permisions import IsAdminOrReadOnly, IsReviewAuthorOrReadOnly
from .serializers import ReviewSerializer, EbookSerializer


# API view for listing and creating Ebook instances
class EbookListCreateAPIView(generics.ListCreateAPIView):
    """
    Handles GET requests to list all Ebook instances
    and POST requests to create a new Ebook.
    """
    queryset = Ebook.objects.all()  # Retrieves all Ebook instances from the database
    serializer_class = EbookSerializer  # Specifies the serializer class for Ebook instances
    permission_classes = [IsAdminOrReadOnly]  # Allows only admin users to create or update, read-only for others


# API view for retrieving, updating, and deleting a specific Ebook instance
class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles GET requests to retrieve a specific Ebook instance,
    PUT/PATCH requests to update, and DELETE requests to remove it.
    """
    queryset = Ebook.objects.all()  # Retrieves all Ebook instances from the database
    serializer_class = EbookSerializer  # Specifies the serializer class for Ebook instances
    permission_classes = [IsAdminOrReadOnly]  # Allows only admin users to modify, read-only for others


# API view for listing and creating Review instances
class ReviewListCreateAPIView(generics.ListCreateAPIView):
    """
    Handles GET requests to list all Review instances associated with an Ebook,
    and POST requests to create a new Review for an Ebook.
    """
    serializer_class = ReviewSerializer  # Specifies the serializer class for Review instances

    def get_queryset(self):
        """
        Filters and returns the reviews for the specified Ebook (ebook_pk).
        Authenticated users can only view their own reviews; anonymous users see none.
        """
        ebook_pk = self.kwargs.get('ebook_pk')  # Gets the ebook ID from the URL parameters
        if self.request.user.is_authenticated:
            # Return reviews for this Ebook from the currently logged-in user
            return Review.objects.filter(ebook__pk=ebook_pk, review_author=self.request.user)
        else:
            # If the user is not authenticated, return an empty queryset
            return Review.objects.none()

    def perform_create(self, serializer):
        """
        Ensures that a user can only create a single review per Ebook. If the user 
        has already reviewed the Ebook, an error is raised.
        """
        ebook_pk = self.kwargs.get('ebook_pk')  # Gets the ebook ID from the URL parameters
        # Retrieve the Ebook instance, raise a 404 error if not found
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        review_author = self.request.user  # Get the currently logged-in user as the review author
        # Check if a review by this user already exists for the Ebook
        review_queryset = Review.objects.filter(ebook=ebook, review_author=review_author)
        if review_queryset.exists():
            # If a review already exists, raise a validation error
            raise ValidationError("You have already reviewed this book.")
        else:
            # Save the review with the current Ebook and user as the author
            serializer.save(ebook=ebook, review_author=review_author)


# API view for retrieving, updating, and deleting a specific Review instance
class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles GET requests to retrieve a specific Review instance,
    PUT/PATCH requests to update it, and DELETE requests to remove it.
    Only the review author can modify or delete the review.
    """
    queryset = Review.objects.all()  # Retrieves all Review instances from the database
    serializer_class = ReviewSerializer  # Specifies the serializer class for Review instances
    permission_classes = [IsReviewAuthorOrReadOnly]  # Restricts modification access to the review author

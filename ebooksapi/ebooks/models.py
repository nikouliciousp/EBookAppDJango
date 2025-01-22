from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Ebook(models.Model):
    """
    Model representing an Ebook.

    Attributes:
        title (str): The title of the Ebook.
        author (str): The author of the Ebook.
        description (TextField): The description of the Ebook.
        publication_date (DateField): The publication date of the Ebook.
    """

    title = models.CharField(max_length=100)  # Title of the Ebook, max length of 100 characters
    author = models.CharField(max_length=100)  # Author's name, max length of 100 characters
    description = models.TextField()  # Detailed description of the Ebook
    publication_date = models.DateField()  # Date the Ebook was published

    def __str__(self):
        # Return the title of the Ebook as its string representation
        return self.title


class Review(models.Model):
    """
    Model representing a review for an Ebook.

    Attributes:
        review_author (ForeignKey): The user who authored the review (linked to User).
        review_date (DateTimeField): The date when the review was created.
        review_updt (DateTimeField): The date when the review was last updated.
        review_text (TextField): The content of the review.
        review_rating (PositiveBigIntegerField): The rating of the Ebook (from 1 to 5).
        ebook (ForeignKey): Reference to the Ebook being reviewed.
    """

    # User who authored the review
    review_author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # Automatically capture the creation date of the review
    review_date = models.DateTimeField(auto_now_add=True)

    # Automatically update the timestamp of the last modification
    review_updt = models.DateTimeField(auto_now=True)

    # The content or text of the review
    review_text = models.TextField()

    # Rating (value between 1 and 5)
    review_rating = models.PositiveBigIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    # Reference to the related Ebook via ForeignKey
    ebook = models.ForeignKey(
        'Ebook', on_delete=models.CASCADE, related_name='reviews'
    )

    class Meta:
        """
        Metadata options for the Review model.
        
        Constraints:
            unique_review: Ensures a unique combination of Ebook and User for reviews.
        """
        constraints = [
            # Unique constraint to ensure a user can review an Ebook only once
            models.UniqueConstraint(fields=['ebook', 'review_author'], name='unique_review')
        ]

    def __str__(self):
        # Return a string representation of the review
        return f"{self.review_author} - {self.review_rating}/5"

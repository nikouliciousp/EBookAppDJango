from ebooks.models import Ebook, Review
from rest_framework import serializers


# Serializer to handle serialization and deserialization of Review model
class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for the Review model, used to convert model instances
    to JSON format and vice versa.
    """

    # Use StringRelatedField to display the author of the review as a string (read-only field)
    review_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('ebook',)  # Exclude the 'ebook' field from serialization and deserialization


# Serializer to handle serialization and deserialization of Ebook model
class EbookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Ebook model, including nested serialization
    of related Review instances.
    """

    # Serialize related Review objects as a nested list of ReviewSerializer objects (read-only field)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Ebook
        fields = '__all__'  # Serialize all fields of the Ebook model

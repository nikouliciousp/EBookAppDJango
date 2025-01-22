from django.urls import path

from .views import EbookListCreateAPIView, EbookDetailAPIView, ReviewListCreateAPIView, ReviewDetailAPIView

urlpatterns = [
    # Endpoint for listing all ebooks or creating a new ebook
    path('ebooks/', EbookListCreateAPIView.as_view(), name='ebook-list'),

    # Endpoint for retrieving, updating, or deleting a specific ebook by its ID
    path('ebooks/<int:pk>/', EbookDetailAPIView.as_view(), name='ebook-detail'),

    # Endpoint for listing or creating reviews for a specific ebook by its ID
    path('ebooks/<int:ebook_pk>/reviews/', ReviewListCreateAPIView.as_view(), name='ebook-reviews'),

    # Endpoint for retrieving, updating, or deleting a specific review by its ID
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail'),
]

# EbooksAPI 📚

EbooksAPI is a RESTful API built with Django and Django REST Framework (DRF) for managing ebooks and their reviews. It offers CRUD operations for ebooks and their reviews while incorporating advanced features like custom permissions, pagination, and object-level validation.

## Features ✨

- **Ebooks Management**: Add, update, retrieve, and delete ebooks.
- **Review System**: Users can leave reviews for ebooks, rate them, and update their own reviews.
- **Custom Permissions**: 
  - Admin users have full write access.
  - Non-admin users have read-only access to ebook data.
  - Only review authors can modify their reviews.
- **Pagination**: Paginated responses with customizable page size.
- **Validation**: Enforces unique reviews per user per ebook.

## Tech Stack 🛠

- **Backend Framework**: Django 5.1
- **API Framework**: Django REST Framework (DRF)
- **Database**: SQLite (default, easily configurable to other databases)
- **Authentication**: Token-based (via `api-auth` endpoint).

## Installation & Setup 🚀

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ebooksapi.git
   cd ebooksapi
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate      # For Windows
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the API:**
   Open your browser and navigate to `http://127.0.0.1:8000/api/`.

## API Endpoints 📖

| Method | Endpoint                                  | Description                                     |
|--------|------------------------------------------|------------------------------------------------|
| GET    | `/api/ebooks/`                           | List all ebooks.                               |
| POST   | `/api/ebooks/`                           | Add a new ebook (admin-only).                 |
| GET    | `/api/ebooks/<int:pk>/`                  | Retrieve a specific ebook.                    |
| PUT    | `/api/ebooks/<int:pk>/`                  | Update an existing ebook (admin-only).        |
| DELETE | `/api/ebooks/<int:pk>/`                  | Delete an ebook (admin-only).                 |
| GET    | `/api/ebooks/<int:ebook_pk>/reviews/`    | List all reviews for a specific ebook.        |
| POST   | `/api/ebooks/<int:ebook_pk>/reviews/`    | Add a review for a specific ebook.            |
| GET    | `/api/reviews/<int:pk>/`                 | Retrieve a specific review.                   |
| PUT    | `/api/reviews/<int:pk>/`                 | Update a specific review (only author).       |
| DELETE | `/api/reviews/<int:pk>/`                 | Delete a specific review (only author).       |

## Models 🛠

### Ebook
An Ebook has the following fields:
- **`title`**: Title of the ebook.
- **`author`**: Author's name.
- **`description`**: A detailed description of the ebook.
- **`publication_date`**: The date the ebook was published.

### Review
A Review has the following fields:
- **`review_author`**: Reference to the user who created the review.
- **`review_date`**: Date when the review was created.
- **`review_updt`**: Date when the review was last updated.
- **`review_text`**: Text content of the review.
- **`review_rating`**: Numeric rating of the ebook (1-5).
- **`ebook`**: Reference to the related Ebook.

## Permissions 🛡

1. **IsAdminOrReadOnly**:
   - Admin users can perform all actions (read-write).
   - Non-admin users can only perform read operations (GET requests).

2. **IsReviewAuthorOrReadOnly**:
   - Review authors can edit or delete their reviews.
   - Other users can only read the reviews.

## Pagination

The API uses **page-based pagination**, with a default page size of 5 items. You can customize the page size in the `settings.py` file.

## Contributing 🤝

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a branch for your feature/fix.
3. Commit your changes and push them to the branch.
4. Submit a pull request.

## License 📝

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## Contact 📩

If you have any questions, feel free to open an issue or reach me at `nikouliciousp@gmail.com`.
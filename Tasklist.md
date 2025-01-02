# ShareILM Task Manager

## Categories

<details>
<summary>1.Project Setup</summary>

- [ ] 1.Fork and clone the ShareILM repository.
- [ ] 2.Set up a virtual environment using `venv` or `pipenv`.
- [ ] 3.Install all dependencies listed in `requirements.txt`.
- [ ] 4.Create a `.env` file and configure database settings.
- [ ] 5.Run initial migrations and verify the database is connected.
- [ ] 6.Test the development server by running `python manage.py runserver`.
- [ ] 7.Document the setup process in the README file under a new "Local Setup" section.
- [ ] 8.Set up `django-environ` for managing environment variables securely.
- [ ] 9.Create a superuser for admin access.
- [ ] 10.Configure static and media file settings for local development.

</details>

<details>
<summary>2.Models</summary>

- [ ] 11.Review the existing models and write comments explaining each field.
- [ ] 12.Create a `Book` model with fields: `title`, `author`, `publisher`, `ISBN`, `price`, `stock`, `category`, and `cover_image`.
- [ ] 13.Create a `Category` model with fields: `name`, `slug`, and `description`.
- [ ] 14.Add a foreign key from the `Book` model to the `Category` model.
- [ ] 15.Create a `Borrower` model with fields: `user`, `borrowed_books`, `due_date`, and `return_status`.
- [ ] 16.Add custom model methods in `Book` for checking stock availability.
- [ ] 17.Implement a `Transaction` model to log book purchases and borrowings.
- [ ] 18.Write a migration script for the new models.
- [ ] 19.Add unit tests for all custom model methods.
- [ ] 20.Test the models using Django’s shell.
- [ ] 21.Create a custom Django command to populate `Book` and `Category` models with sample data using `faker`.
- [ ] 22.Add fixtures for `Book` and `Category` models to preload sample data into the database.

</details>

<details>
<summary>3.Views and URLs</summary>

- [ ] 23.Create a view for listing all books with pagination.
- [ ] 24.Build a detail view for individual books.
- [ ] 25.Implement a search functionality for books based on title, author, or ISBN.
- [ ] 26.Add a view to list books by category.
- [ ] 27.Write URLs for all book-related views.
- [ ] 28.Implement breadcrumb navigation for better user experience.
- [ ] 29.Create a view for users to borrow books and track borrow status.
- [ ] 30.Add a dashboard view for administrators to manage stock levels.
- [ ] 31.Optimize querysets in views for better performance.

</details>

<details>
<summary>4.Templates</summary>

- [ ] 32.Design a base template with a consistent header, footer, and sidebar.
- [ ] 33.Create a homepage template showing featured and recently added books.
- [ ] 34.Add a book detail template displaying book information and stock status.
- [ ] 35.Create a search results template for books.
- [ ] 36.Implement a template to display book categories with thumbnails.
- [ ] 37.Write a custom template filter for formatting book prices.
- [ ] 38.Create a responsive template for the "My Borrowed Books" page.
- [ ] 39.Test the templates on mobile and desktop devices.

</details>

<details>
<summary>5.Testing</summary>

- [ ] 40.Write tests for the setup script to ensure local configurations work.
- [ ] 41.Add unit tests for all custom model methods.
- [ ] 42.Create integration tests for book-related views.
- [ ] 43.Test the responsiveness of templates on different devices.
- [ ] 44.Automate regression testing for updates.

</details>

<details>
<summary>6.Hard Tools (Docker and Others)</summary>

- [ ] 45.Add a `docker-compose.yml` file for local development setup with PostgreSQL.
- [ ] 46.Test the Docker setup by running `docker-compose up`.
- [ ] 47.Document the Docker setup process.
- [ ] 48.Write Docker health checks for critical services.
- [ ] 49.Optimize Dockerfile for faster build times.

</details>

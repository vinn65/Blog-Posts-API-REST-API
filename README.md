# Django Blog Project

This is a simple blog application built with Django. It supports categories, blog posts, comments (with threaded replies), and an excerpt feature for posts. The project also uses auto-slug generation for both blog posts and categories.

## Features

- Create and manage blog posts with categories.
- Add comments to blog posts, with support for threaded replies.
- Automatically generate slugs for blog posts and categories.
- Show main, recent, and popular blog posts on the homepage.
- Filter blog posts by categories.
- Blog post excerpt support.

## Models

### `Category`

- **name**: The name of the category.
- **slug**: A unique, auto-generated slug for the category.

### `Blog`

- **title**: The title of the blog post.
- **author**: The author of the blog post.
- **image**: Image associated with the post.
- **content**: Main content of the blog post.
- **category**: ForeignKey to `Category`.
- **blog_slug**: Auto-generated slug based on the title.
- **date**: Date when the blog post is published.
- **status**: Draft or Publish status.
- **section**: Post section (Recent, Publish, Trending).
- **main_post**: Boolean to indicate if the post is the main featured post.
- **excerpt**: Method to generate an excerpt from the content.

### `Comment`

- **post**: ForeignKey to `Blog`.
- **name**: Name of the commenter.
- **email**: Email of the commenter.
- **website**: Optional website of the commenter.
- **comment**: The comment text.
- **date**: Date and time the comment was posted.
- **parent**: Optional self-referential ForeignKey for comment replies.

## Views

### `index`

This view renders the homepage with various blog listings:
- **Main_post**: A featured post.
- **Recent**: The 5 most recent blog posts.
- **Popular**: Top 3 trending blog posts.
- **Categories**: A list of all blog categories with a post count.

### `blog_detail`

This view displays the full details of a blog post, along with the associated comments:
- **post**: The selected blog post.
- **comments**: Comments associated with the blog post.

### `category`

This view displays blog posts filtered by a specific category:
- **active_category**: The selected category.
- **blogs_in_category**: Blog posts that belong to the selected category.

### `add_comment`

This view handles adding a comment to a blog post:
- **post**: The blog post to which the comment is added.
- **name**: Name of the commenter.
- **email**: Email of the commenter.
- **website**: Optional website of the commenter.
- **comment_text**: The comment text.
- **parent_comment**: Optional parent comment for threading.

## Templates

### `index.html`

Displays the main page with various blog listings such as featured posts, recent posts, and categories.

### `blog_detail.html`

Displays the full blog post with the comment section.



Displays the blog posts filtered by category.

## Installation

1. Clone the repository:

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Django migrations:
    ```bash
    python manage.py migrate
    ```
4. Create a superuser to access the admin panel:
    ```bash
    python manage.py createsuperuser
    ```
5. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

- Navigate to `http://127.0.0.1:8000/` to view the homepage.
- Navigate to `http://127.0.0.1:8000/admin` to manage blog posts, categories, and comments from the Django admin panel.

## Live website
  https://blog-posts-api-rest-api-2.onrender.com/
## Admin
  /admin/
  admin creds - username : admin, pass - admin@123

## Future work - adding an api, adding user accounts * not staff, customizing admin dashboard, etc
  

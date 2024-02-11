# Django REST Framework Project Documentation

## Users App

### Register User

- **URL:** `/api/v2/auth/register/`
- **Method:** `POST`
- **Description:** Register a new user.

---

### Current User

- **URL:** `/api/v2/auth/me/`
- **Method:** `GET`
- **Description:** Get details of the currently logged-in user.

---

### Obtain Token Pair

- **URL:** `/api/v2/auth/token/`
- **Method:** `POST`
- **Description:** Obtain an access token and a refresh token by providing valid credentials.

---

### Refresh Token

- **URL:** `/api/v2/auth/token/refresh/`
- **Method:** `POST`
- **Description:** Refresh an access token by providing a valid refresh token.

---

### Verify Token

- **URL:** `/api/v2/auth/token/verify/`
- **Method:** `POST`
- **Description:** Verify the validity of an access token.

---

## Product App

### All Products (Paginated)

- **URL:** `/api/v2/products-paginate/`
- **Method:** `GET`
- **Description:** Retrieve all products in a paginated format.

---

### Search Products

- **URL:** `/api/v2/products-query/`
- **Method:** `GET`
- **Description:** Search for products based on query parameters.

---

### Product List and Creation

- **URL:** `/api/v2/products/`
- **Method:** `GET`, `POST`
- **Description:** List all products and create a new product.

---

### Product CRUD Operations

- **URL:** `/api/v2/product-admin/`
- **Method:** `GET`, `POST`, `PUT`, `PATCH`, `DELETE`
- **Description:** Perform CRUD operations on products for admin users.

---

### Product Images Update and Delete

- **URL:** `/api/v2/images/<int:pk>/`
- **Method:** `GET`, `POST`, `DELETE`
- **Description:** Update or delete product images.

---

### Generate Category

- **URL:** `/api/v2/all-category/`
- **Method:** `GET`
- **Description:** Retrieve all categories.

---

## Miscellaneous

### Django Admin Interface

- **URL:** `/admin/`
- **Description:** Access the Django admin interface.

---

### API Root

- **URL:** `/api/v2/`
- **Description:** API root endpoint.

---

### Media URLs (Debug Mode Only)

- **URL:** `/media/`
- **Description:** Serve media files in debug mode.


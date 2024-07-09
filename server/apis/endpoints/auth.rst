
=======================
Authentication API
=======================

**User Login**

**Endpoint:** `/api/auth/login`

**Method:** `POST`

**Description:**
The User Authentication API allows users to log in to the platform. Users need to provide their username and password to authenticate.

**Request:**
.. code-block:: json

   {
     "username": "your_username",
     "password": "your_password"
   }

**Responses:**

- `200 OK`: User successfully logged in.
- `400 Bad Request`: User already logged in.
- `401 Unauthorized`: Invalid username or password.


**User Logout API**

**Endpoint:** `/api/auth/logout`

**Method:** `POST`

**Description:**
The User Logout API allows users to log out of the platform. This endpoint does not require any parameters.

**Responses:**

- `200 OK`: User successfully logged out.

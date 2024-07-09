===========================
Create User API
===========================

**Endpoint:** `/users/`

**Method:** `POST`

**Description:**
The Create User API allows for the creation of a new user by providing a username, password, and account type.

**Parameters:**

- `username` (string, required): Username cannot be blank
- `password` (string, required): Password cannot be blank
- `account_type` (string, required): Account type cannot be blank

**Responses:**

- `201 Created`: User successfully created.
- `400 Bad Request`: Invalid data provided in request.


===========================
Get All Users API
===========================

**Endpoint:** `/users/`

**Method:** `GET`

**Description:**
The Get All Users API retrieves a list of all users.

**Parameters:**

None

**Responses:**

- `200 OK`: Success


===========================
Delete User API
===========================

**Endpoint:** `/users/`

**Method:** `DELETE`

**Description:**
The Delete User API allows an admin to delete a user from the database by providing the username.

**Parameters:**

- `username` (string, required): The username to delete

**Responses:**

- `200 OK`: User successfully deleted.
- `400 Bad Request`: Invalid data provided in request.


===========================
Check Username Availability API
===========================

**Endpoint:** `/users/check/{username}`

**Method:** `GET`

**Description:**
The Check Username Availability API checks if a username is available.

**Parameters:**

- `username` (string, path): The username to check

**Responses:**

- `200 OK`: Success


===========================
Update User Type API
===========================

**Endpoint:** `/users/{user_id}/type`

**Method:** `POST`

**Description:**
The Update User Type API allows updating the account type of a user.

**Parameters:**

- `account_type` (string, required): Account type cannot be blank
- `user_id` (string, path): The user ID

**Responses:**

- `200 OK`: User type successfully updated.
- `400 Bad Request`: Invalid data provided in request.


===========================
Get Profile Picture API
===========================

**Endpoint:** `/users/{username}/profile_picture/`

**Method:** `GET`

**Description:**
The Get Profile Picture API retrieves the profile picture of a user by their username.

**Parameters:**

- `username` (string, path): The username whose profile picture is to be retrieved.

**Responses:**

- `200 OK`: Profile picture successfully retrieved.


===========================
Get Profile Picture Thumbnail API
===========================

**Endpoint:** `/users/{username}/thumbnail/`

**Method:** `GET`

**Description:**
The Get Profile Picture Thumbnail API retrieves the thumbnail version of a user's profile picture by their username.

**Parameters:**

- `username` (string, path): The username whose profile picture thumbnail is to be retrieved.

**Responses:**

- `200 OK`: Profile picture thumbnail successfully retrieved.

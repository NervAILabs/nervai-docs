===========================
Settings API
===========================


===========================
Update Password API
===========================

**Endpoint:** `/settings/update_password`

**Method:** `POST`

**Description:**
The Update Password API allows users to change their password by providing the old password and the new password.

**Parameters:**

- `new_password` (string, required): Enter new password
- `old_password` (string, required): Enter old password

**Responses:**

- `200 OK`: Success


===========================
Update User Settings API
===========================

**Endpoint:** `/settings/update_user_settings`

**Method:** `POST`

**Description:**
The Update User Settings API allows users to update their personal settings, such as name and email.

**Parameters:**

- `name` (string, required): The
- `email` (string, required): The email address

**Responses:**

- `200 OK`: Success

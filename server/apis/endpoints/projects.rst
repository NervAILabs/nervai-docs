=======================
Create New Project API
=======================

**Endpoint:** `/projects/`

**Method:** `POST`

**Description:**
The Create New Project API allows users to create a new project by providing project name, description, type, and task.

**Parameters:**

- `project-name` (string, query, required): Project name
- `project-description` (string, query, required): Project description
- `project-type` (string, query, required): Project type
- `project-task` (string, query, required): Project task

**Responses:**

- `200 OK`: Success



=======================
List All Projects API
=======================

**Endpoint:** `/projects/`

**Method:** `GET`

**Description:**
The List All Projects API retrieves a list of all projects.

**Parameters:**

- `X-Fields` (string, header): An optional fields mask

**Responses:**

- `200 OK`: Success



=======================
Get Project Criteria Name API
=======================

**Endpoint:** `/projects/criteria`

**Method:** `GET`

**Description:**
The Get Project Criteria Name API retrieves the criteria name for projects.

**Parameters:**
None

**Responses:**

- `200 OK`: Success



=======================
Get Project Details API
=======================

**Endpoint:** `/projects/{project_id}`

**Method:** `GET`

**Description:**
The Get Project Details API retrieves details of a specified project.

**Parameters:**

- `X-Fields` (string, header): An optional fields mask
- `project_id` (string, path, required): The ID of the project

**Responses:**

- `200 OK`: Success



=======================
Delete Project API
=======================

**Endpoint:** `/projects/{project_id}`

**Method:** `DELETE`

**Description:**
The Delete Project API allows users to delete a specified project.

**Parameters:**

- `project_id` (string, path, required): The ID of the project

**Responses:**

- `200 OK`: Success



=======================
Get List of Project Configs API
=======================

**Endpoint:** `/projects/{project_id}/configs`

**Method:** `GET`

**Description:**
The Get List of Project Configs API retrieves a list of configurations for a specified project.



=======================
Get Details of Project Config API
=======================

**Endpoint:** `/projects/{project_id}/configs/{config_id}`

**Method:** `GET`

**Description:**
The Get Details of Project Config API retrieves details of a specified project configuration.


=======================
Get Details of Project Config API
=======================

**Endpoint:** `/projects/{project_id}/configs/{config_id}`

**Method:** `GET`

**Description:**
The Get Details of Project Config API retrieves details of a specified project configuration.

=======================
Get Project Graph API
=======================

**Endpoint:** `/projects/{project_id}/configs/{config_id}/graph`

**Method:** `GET`

**Description:**
The Get Project Graph API retrieves the graph representation of a specified project configuration.


=======================
Get Project Environment Details API
=======================

**Endpoint:** `/projects/{project_id}/environment`

**Method:** `GET`

**Description:**
The Get Project Environment Details API retrieves the environment details of a specified project.


=======================
Update Project Environment Details API
=======================

**Endpoint:** `/projects/{project_id}/environment`

**Method:** `PUT`

**Description:**
The Update Project Environment Details API allows users to update the environment details of a specified project.

**Parameters:**

- `entry_point_command` (string, query, required): Entry point command
- `env_type` (string, query, required): Environment type
- `dependencies` (string, query, required): Dependencies
- `project_id` (string, path, required): The ID of the project

**Responses:**

- `200 OK`: Success


=======================
Get List of Project Experiments API
=======================

**Endpoint:** `/projects/{project_id}/experiments`

**Method:** `GET`

**Description:**
The Get List of Project Experiments API retrieves a list of experiments for a specified project.


=======================
Train Project API
=======================

**Endpoint:** `/projects/{project_id}/train`

**Method:** `POST`

**Description:**
The Train Project API allows users to train a specified project using a provided configuration file.

**Parameters:**

- `config` (string, query, required): Configuration file name
- `project_id` (string, path, required): The ID of the project

**Responses:**

- `200 OK`: Success


=======================
Train Project Remotely API
=======================

**Endpoint:** `/projects/{project_id}/train-remote`

**Method:** `POST`

**Description:**
The Train Project Remotely API allows users to train a specified project on a remote cluster.

**Parameters:**

- `project_id` (string, path, required): The ID of the project

**Responses:**

- `200 OK`: Success

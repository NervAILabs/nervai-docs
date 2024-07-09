=======================
Integrations API
=======================

---------------------------------------
GitHub Integration API
---------------------------------------



**Endpoint:** `/integrations/github`

**Method:** `POST`

**Description:**
The GitHub Integration API enables or updates GitHub integration by providing a valid GitHub username.

**Request:**
.. code-block:: json

   {
     "github_username": "your_github_username"
   }

**Responses:**

- `200 OK`: Success
- `400 Bad Request`: Invalid GitHub username
- `401 Unauthorized`: Access denied


---------------------------------------
Check GitHub Integration Status API
---------------------------------------


**Endpoint:** `/integrations/github`

**Method:** `GET`

**Description:**
The Check GitHub Integration Status API retrieves the current status of the GitHub integration.

**Responses:**

- `200 OK`: Success
- `401 Unauthorized`: Access denied


---------------------------------------
Disable GitHub Integration API
---------------------------------------


**Endpoint:** `/integrations/github`

**Method:** `DELETE`

**Description:**
The Disable GitHub Integration API removes the GitHub integration for the user.

**Responses:**

- `200 OK`: Success
- `401 Unauthorized`: Access denied


---------------------------------------
DFKI SLURM Integration API
---------------------------------------

**Endpoint:** `/integrations/slurm`

**Method:** `POST`

**Description:**
The DFKI SLURM Integration API enables or updates SLURM integration by providing the DFKI SLURM username, DFKI SLURM password, and VisualML password.

**Request:**
.. code-block:: json

   {
     "dfki_username": "your_dfki_username",
     "dfki_password": "your_dfki_password",
     "vml_password": "your_vml_password"
   }

**Responses:**

- `200 OK`: Success
- `401 Unauthorized`: Access denied
- `500 Internal Server Error`: Internal server error


---------------------------------------
Check SLURM Integration Status API
---------------------------------------


**Endpoint:** `/integrations/slurm`

**Method:** `GET`

**Description:**
The Check SLURM Integration Status API retrieves the current status of the SLURM integration.

**Responses:**

- `200 OK`: Success
- `401 Unauthorized`: Access denied
- `500 Internal Server Error`: Internal server error


---------------------------------------
List SLURM Containers API
---------------------------------------

**Endpoint:** `/integrations/slurm/containers`

**Method:** `GET`

**Description:**
The List SLURM Containers API retrieves a list of all enroot containers on the SLURM cluster.

**Responses:**

- `200 OK`: Success


---------------------------------------
Get SLURM Jobs API
---------------------------------------


**Endpoint:** `/integrations/slurm/jobs`

**Method:** `GET`

**Description:**
The Get SLURM Jobs API retrieves a list of queued jobs for the current user.

**Responses:**

- `200 OK`: Success


---------------------------------------
List SLURM Partitions API
---------------------------------------


**Endpoint:** `/integrations/slurm/partitions`

**Method:** `GET`

**Description:**
The List SLURM Partitions API retrieves details of available partitions.

**Responses:**

- `200 OK`: Success


---------------------------------------
Submit SLURM Job API
---------------------------------------


**Endpoint:** `/integrations/slurm/submit`

**Method:** `POST`

**Description:**
The Submit SLURM Job API allows users to submit a job to the SLURM scheduler by providing project ID, partition, number of GPUs, number of CPUs, and the config file path.

**Request:**
.. code-block:: json

   {
     "project_id": "your_project_id",
     "partition": "your_partition",
     "num_gpu": 1,
     "num_cpu": 4,
     "config": "path_to_config_file"
   }

**Responses:**

- `200 OK`: Success

.. image:: /mnt/data/file-fBBKEpUOH5U8VXmPtTNCtJwY.png
   :alt: Swagger documentation for Submit SLURM Job API
   :align: center



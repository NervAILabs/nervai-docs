
=======================
Datasets
=======================

---------------------------------------
List Datasets for a Task API
---------------------------------------

**Endpoint:** `/datasets/{task}`

**Method:** `GET`

**Description:**
The List Datasets for a Task API retrieves all datasets related to a specified task.

**Parameters:**

- `category` (string, query): Pose dataset category name
- `task` (string, path, required): The task for which to list datasets

**Responses:**

- `200 OK`: Success


---------------------------------------
Get Dataset for a Task API
---------------------------------------


**Endpoint:** `/datasets/{task}/{dataset_name}`

**Method:** `GET`

**Description:**
The Get Dataset for a Task API retrieves a specific dataset related to a specified task.

**Parameters:**

- `task` (string, path, required): The task for which to get the dataset
- `dataset_name` (string, path, required): The name of the dataset

**Responses:**

- `200 OK`: Success

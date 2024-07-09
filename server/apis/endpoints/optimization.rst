=======================
Quantization and Pruning APIs
=======================

**Create Pruning Strategies API**

**Endpoint:** `/optimization/prune`

**Method:** `POST`

**Description:**
The Create Pruning Strategies API allows users to create pruning strategies for model optimization.

**Parameters:**

- `model_name` (string, query, required): Model name
- `inputs` (string, query, required): Shapes of the input tensors (comma-separated)
- `outputs` (string, query, required): Shapes of the output tensors (comma-separated)
- `strategy` (string, query, required): Pruning strategy
- `compression` (integer, query): Compression factor (Default value: 1)
- `X-Fields` (string, header): An optional fields mask

**Responses:**

- `200 OK`: Success


**List All Pruning Strategies API**

**Endpoint:** `/optimization/prune/strategies`

**Method:** `GET`

**Description:**
The List All Pruning Strategies API retrieves a list of all pruning strategies.

**Responses:**

- `200 OK`: Success


**Create Quantization Strategies API**

**Endpoint:** `/optimization/quantize`

**Method:** `POST`

**Description:**
The Create Quantization Strategies API allows users to create quantization strategies for model optimization.

**Parameters:**

- `model_name` (string, query, required): Model name
- `strategy` (string, query, required): Quantization strategy
- `quant_type` (string, query): Quantization type
- `precision` (integer, query, required): Quantization precision
- `leaf_node` (boolean, query): Quantize leaf nodes only (Default value: false)
- `X-Fields` (string, header): An optional fields mask

**Responses:**

- `200 OK`: Success


**List All Quantization Strategies API**

**Endpoint:** `/optimization/quantize/strategies`

**Method:** `GET`

**Description:**
The List All Quantization Strategies API retrieves a list of all quantization strategies.

**Responses:**

- `200 OK`: Success

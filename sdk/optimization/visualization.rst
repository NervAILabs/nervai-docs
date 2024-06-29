=======================================
Inspecting Model Architectures
=======================================

The visualization module provides functionalities to visualize neural network models and calculate their structural properties.


=====================================
Computational Graph
=====================================

This section covers the ``draw_graph`` and ``calculate_max_depth`` functions.

----------
draw_graph
----------

The ``draw_graph`` function generates a visual representation of a PyTorch model's computational graph. This visualization includes modules, module hierarchies, torch functions, and tensor shapes captured during forward propagation.

**Usage**

.. code-block:: python

    from visualml.visualization import draw_graph, calculate_max_depth

    # Example model
    model = YourModel()

    # Calculate the maximum depth of the model
    depth = calculate_max_depth(model)

    # Create model graph with maximum depth
    graph = draw_graph(model, input_size=(1, 3, 224, 224), depth=depth, device='cpu')


**Parameters**

- ``model``: The PyTorch model to be visualized.
- ``input_data``: Optional. The input data for the model's forward method. Wrap it in a list for multiple arguments or a dictionary for named arguments.
- ``input_size``: The shape of the input data as a list, tuple, or torch.Size. This is used if no direct input_data is provided.
- Additional parameters control the visual appearance and behavior of the generated graph, such as ``depth`` for controlling the visualization depth and ``device`` for specifying the computation device.

**Returns**

- A ``ComputationGraph`` object that includes the visualization of the PyTorch model.

-------------------
calculate_max_depth
-------------------

The ``calculate_max_depth`` function computes the maximum depth of a PyTorch model. This information is useful for visualizing models with ``draw_graph``, ensuring that the graph depth is appropriate for the model's complexity.

**Usage**

.. code-block:: python

    from visualml.visualization import calculate_max_depth

    # Example model
    model = YourModel()

    # Calculate the maximum depth of the model
    depth = calculate_max_depth(model)

**Parameters**

- ``model``: The PyTorch model whose depth is to be calculated.
- ``depth``: Optional. Initial depth level, default is 0. Used internally for recursive depth calculation.


=====================================
Quantization
=====================================

Quantization is a process that reduces the precision of the weights and activations of a neural network, converting them from floating point to lower precision formats like integer or fixed point. This can significantly reduce the model size and increase inference speed, while aiming to maintain the original model's accuracy.

------------------------------
Using the Quantization Package
------------------------------

The quantization package offers a straightforward API to apply various quantization strategies to your neural network models. 

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Listing Available Quantization Strategies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
First, to see which quantization strategies are available, use the `list_quantization_strategies` function:

.. code-block:: python

    from visualml.optimization import list_quantization_strategies

    # List all available quantization strategies
    strategies = list_quantization_strategies()
    print(strategies)

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Quantizing a Model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To quantize a model, you will use the `quantize` function. This function requires specifying the model, the quantization strategy, the type of quantization, and the precision level.

.. code-block:: python

    from visualml.optimization import quantize

    # Example: Quantizing a model using Weight-Only Quantization to float16
    quantized_model = quantize(model, 'WeightOnlyQuantization', 'float', 16)
    print(quantized_model)

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Layer-wise Quantization Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Quantizing specific layers individually can also be achieved using the `quantize_layer` function. This is particularly useful for applying different quantization strategies or precisions to different parts of the model.

.. code-block:: python

    from visualml.optimization import quantize_layer

    # Example: Quantizing a specific layer of the model
    quantized_layer = quantize_layer(node_id, 'WeightOnlyQuantization', 'float', 16, comp_graph)
    print(quantized_layer)


---------------------------------
Quantization Strategies Explained
---------------------------------

Here is an overview of the quantization strategies available:

- **WeightOnlyQuantization**: Quantizes only the weights of the model to the specified precision.
- **WeightBiasQuantization**: Quantizes both weights and biases of the model.
- **ActivationOnlyQuantization**: Applies quantization only to the activations during inference.
- **WeightBiasActivationQuantization**: Quantizes weights, biases, and activations of the model, offering a comprehensive quantization approach.

Each strategy targets different components of the neural network for quantization, allowing for flexibility in balancing model size, performance, and accuracy.

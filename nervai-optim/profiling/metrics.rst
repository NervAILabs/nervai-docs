================================================
Profiling Metrics
================================================

Profiling metrics are crucial for understanding the performance characteristics of your model. They help identify bottlenecks and optimize model architecture and execution.

The functional API provides a straightforward way to profile different aspects of your model. Here is an overview of the functions available:

- **profile_metrics**: Profiles multiple metrics of the model, including MACs, FLOPs, runtime, memory usage, MAdds, and parameters.
- **profile_macs**: Profiles the Multiply-Accumulates operations of the model.
- **profile_flops**: Profiles the Floating Point Operations per Second of the model.
- **profile_runtime**: Measures the runtime of the model.
- **profile_memory**: Measures the memory usage of the model.
- **profile_madds**: Profiles the Multiply-Add operations of the model.
- **profile_params**: Counts the number of parameters in the model.

Each of these functions requires the model and the input shape as arguments. Some functions allow for additional parameters such as `readable`, which provides output in a human-readable format.

.. code-block:: python

    # Example of profiling model parameters in a readable format
    params = profile_params(model, input_shape=(3, 224, 224), readable=True)

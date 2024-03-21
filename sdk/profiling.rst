================================================
Profiling
================================================

The profiling API provides a comprehensive suite of tools for measuring various aspects of model performance, including memory usage, computational complexity, and runtime. This documentation covers the profiling functions available in the Metinor package for deep learning models.

To begin profiling your model, first import the necessary functions from the profiler:

.. code-block:: python

    from metinor.profiler.functional import profile_metrics, profile_macs, profile_flops, profile_runtime, profile_memory, profile_madds, profile_params
    from metinor.profiler.metrics import MetricType
    from metinor.profiler import ProfilerReport, Profiler
    from metinor.profiler.analysis import ReportAnalyzer

---------------------------------------
Profiling Metrics
---------------------------------------

Profiling metrics are crucial for understanding the performance characteristics of your model. They help identify bottlenecks and optimize model architecture and execution.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Functional API for Profiling
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

---------------------------------------
Profiler Class and Report
---------------------------------------

For a more detailed and integrated profiling experience, Metinor offers the `Profiler` class. This class facilitates comprehensive profiling and generates a `ProfilerReport`, which includes a detailed breakdown of performance metrics.

- **Profiler**: A class used to profile the model comprehensively.
- **ProfilerReport**: Contains the results of profiling, including summaries and detailed breakdowns of metrics.

To use the Profiler, instantiate it with the model and input shape, and then call the `profile` method:

.. code-block:: python

    profiler = Profiler(model, input_shape=(3, 224, 224))
    profiled_nodes = profiler.profile()
    report = ProfilerReport(profiled_nodes)

---------------------------------------
Analyzing Profiling Results
---------------------------------------

The `ReportAnalyzer` class provides tools for analyzing and visualizing the profiling results. It offers methods for identifying layers with high resource usage, understanding the impact of each layer, and filtering layers by type.

- **ReportAnalyzer**: A class for analyzing profiling reports, offering methods for searching, filtering, and plotting results.

.. code-block:: python

    analyzer = ReportAnalyzer(report)
    top_flops_layers = analyzer.find_top_n_layers(MetricType.FLOPS, n=5)

The analyzer also supports plotting capabilities to visualize the profiling results, such as memory usage and layer-wise impacts.



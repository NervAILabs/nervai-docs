================================================
Profiler Reports
================================================

For a more detailed and integrated profiling experience, Metinor offers the `Profiler` class. This class facilitates comprehensive profiling and generates a `ProfilerReport`, which includes a detailed breakdown of performance metrics.

- **Profiler**: A class used to profile the model comprehensively.
- **ProfilerReport**: Contains the results of profiling, including summaries and detailed breakdowns of metrics.

To use the Profiler, instantiate it with the model and input shape, and then call the `profile` method:

.. code-block:: python

    profiler = Profiler(model, input_shape=(3, 224, 224))
    profiled_nodes = profiler.profile()
    report = ProfilerReport(profiled_nodes)

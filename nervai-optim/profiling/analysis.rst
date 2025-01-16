================================================
Analyzing Profiling Results
================================================


The `ReportAnalyzer` class provides tools for analyzing and visualizing the profiling results. It offers methods for identifying layers with high resource usage, understanding the impact of each layer, and filtering layers by type.

- **ReportAnalyzer**: A class for analyzing profiling reports, offering methods for searching, filtering, and plotting results.

.. code-block:: python

    analyzer = ReportAnalyzer(report)
    top_flops_layers = analyzer.find_top_n_layers(MetricType.FLOPS, n=5)

The analyzer also supports plotting capabilities to visualize the profiling results, such as memory usage and layer-wise impacts.

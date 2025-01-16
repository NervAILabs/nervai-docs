=====================================
Profiling Tools
=====================================

The profiling API provides a comprehensive suite of tools for measuring various aspects of model performance, including memory usage, computational complexity, and runtime. This documentation covers the profiling functions available in the Metinor package for deep learning models.

To begin profiling your model, first import the necessary functions from the profiler:

.. code-block:: python

    from nervai_optim.profiler.functional import profile_metrics, profile_macs, profile_flops, profile_runtime, profile_memory, profile_madds, profile_params
    from nervai_optim.profiler.metrics import MetricType
    from nervai_optim.profiler import ProfilerReport, Profiler
    from nervai_optim.profiler.analysis import ReportAnalyzer

.. toctree::

    metrics
    reports
    analysis
    support-matrix/index
    tutorial_1


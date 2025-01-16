=====================================
Optimzation Toolkit
=====================================

The NervAI Optimization Toolkit constitutes an advanced Python package tailored for the profiling, visualization, and optimization of neural network architectures. Its principal objective is to facilitate an in-depth understanding of the memory and computational requirements of PyTorch models, enable intuitive visualization of their structure and intermediate outputs, and apply state-of-the-art optimization techniques for deployment in resource-constrained environments.

Key features of the NervAI Optimization SDK include:

- **Model Inspection** - A suite of tools for detailed visualization, encompassing graph-based representations of network architectures and in-depth analyses of feature maps, filter activations, gradient distributions, and more.
- **Model Profiling** - A robust profiling utility designed to evaluate and report on the memory footprint and computational overhead of neural networks.
- **Model Optimization** - A collection of cutting-edge algorithms for neural network pruning, quantization, and compression to ensure efficient deployment while maintaining model performance.

---------------------------
Installation
---------------------------

The NervAI Optimization Toolkit can be installed from PyPI using the following command:

.. code-block:: bash

    pip install nervai-optim

---------------------------
Documentation
---------------------------

.. toctree::

    inspection/index
    profiling/index
    optimization/index

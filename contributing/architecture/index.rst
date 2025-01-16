======================================
Understanding the System Architecture
======================================

The NervAI Engine project is designed to be a modular and extensible framework for creating visual deep learning pipelines. In this section, we provide an overview of the system architecture and the main components of the NervAI Engine project. This information will help you understand how the different components of the project interact with each other and how you can contribute to the project.

When you clone the NervAI Engine project repository, you will find several subfolders that contain the different components of the project.

.. code-block:: bash

    .
    |── docs: Contains the documentation for the project.
    ├── metinor: Contains the Metinor library.
    ├── vml-sdk: Contains the SDK for the NervAI Engine framework.
    └── vml-server: Contains the Flask web server.
        ├── routes
        │   └── apis: Contains the REST API endpoints.
        └── static
            └── js: Contains the frontend code built using JavaScript.
    └── vml-tracking: Contains the experiment tracking library derived from MLflow Tracking.

Each of these subfolders is a separate Git repository that can be developed and tested independently. The following diagram shows the high-level architecture of the NervAI Engine project, including the main components and their interactions.

.. image:: /images/system/architecture.svg
    :alt: NervAI Engine Architecture
    :align: center
    :width: 100%

These components work together to provide a seamless user experience. The SDK provides an easy-to-use interface for building and training deep learning models, while the server provides a REST API for interacting with the SDK and visualizing the results. The Metinor library provides a set of utilities for working with PyTorch models, and the tracking library allows you to log and track experiments using MLflow.

In the following sections, we will provide more detailed information about each of these components and how they interact with each other.

.. toctree::
   :maxdepth: 2

   metinor
   sdk
   server
   tracking


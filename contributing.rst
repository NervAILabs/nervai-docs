=================================
Contributing
=================================

This contribution guide is intended for developers who want to contribute to the VisualML project. It provides information about the project structure and the overall system architecture to help you understand how the project works. It also explains how to set up the development environment and get started with contributing to the project.

--------------------------------------
The VisualML Design Philosophy
--------------------------------------

The VisualML project is designed to be a modular and extensible framework for creating visual machine learning pipelines. When you clone the repository, you will see that the project is divided into two main components:

- The `vml-sdk` folder contains the SDK, which defines the core functionality of the framework.
- The `vml-server` folder contains the Flask web server, which serves the GUI and acts as the middleware between the GUI and the backend.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The VisualML SDK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The VisualML SDK is the core of the VisualML framework. It provides the functionality to create and manage machine learning pipelines, including data preprocessing, model training, and model evaluation. The SDK is designed to be modular and extensible, allowing developers to easily add new components and customize existing ones.

The SDK is organized into several modules, each of which provides a specific set of functionality. The main modules are:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The VisualML Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The VisualML server is a Flask web server that serves the GUI and acts as the middleware between the GUI and the backend. The server provides a RESTful API that allows the GUI to interact with the backend and perform various operations, such as creating and managing machine learning pipelines.

The server uses a file-based database to store information about the pipelines, including the pipeline configuration, the training data, and the trained models. The server also provides functionality to save and load pipelines from disk, allowing users to persist their work across sessions.

.. warning::
    In the future, the UI will be separated from the server, and the server will be used as a backend API server. The UI will be moved to a separate repository and will be developed as a standalone project.

--------------------------------------
Setting Up the Development Environment
--------------------------------------

Before you can start contributing to the VisualML project, you need to set up your development environment. Please follow the steps in the ::ref:`installation guide <./installation>` to install the required dependencies and set up the project. When installing the project using the ``pip install .`` command, add the ``-e`` flag to install the project in editable mode:

.. code-block:: bash

    pip install -e .

This will allow you to make changes to the project files and see the changes reflected in the installed package without having to reinstall the package.

Next, execute the following commands to install the development dependencies:

.. code-block:: bash

    pip install -r requirements-dev.txt


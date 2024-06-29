======================================
Setting Up the Development Environment
======================================

Before you can start contributing to the VisualML project, you need to set up your development environment. Please follow the steps in the ::ref:`installation guide <./installation>` to install the required dependencies and set up the project. When installing the project using the ``pip install .`` command, add the ``-e`` flag to install the project in editable mode:

.. code-block:: bash

    pip install -e .

This will allow you to make changes to the project files and see the changes reflected in the installed package without having to reinstall the package.

Next, execute the following commands to install the development dependencies:

.. code-block:: bash

    pip install -r requirements-dev.txt
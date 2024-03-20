=================================
Installation
=================================


---------------------------
Prerequisites
---------------------------
This project requires the following dependencies:

- Python 3.8 or higher
- GraphViz

We tested the project on Ubuntu 22.04 LTS.

---------------------------
Cloning the Repository
---------------------------

To get started, clone the repository by running the following command:

.. code-block:: bash

    git clone --recurse-submodules https://github.com/mindgarage-saif/visual-ml.git
    cd visual-ml

.. note::
    TL;DR - For automatic setup, execute `./run.sh` from project root.

---------------------------
Setting up the Environment
---------------------------

To set up the environment, run the following commands:

.. code-block:: bash

    python3 -m venv venv
    source venv/bin/activate
    pip install -U pip wheel

This will create a virtual environment and make sure that the `pip` and `wheel` packages are up-to-date. These packages are required to install the dependencies.


---------------------------
Installing the Dependencies
---------------------------

To install the dependencies, run the following commands:

.. code-block:: bash

    pip install .
    mim install -r requirements-mim.txt

At this point, the environment is set up and the VisualML SDK is installed. Next, you will set up the Flask server for the VisualML web interface by installing the dependencies in the `vml-server` directory.

.. code-block:: bash

    pip install -r vml-server/requirements.txt


---------------------------
Running the Server
---------------------------

To run the server, navigate to the `vml-server` directory and run the following command:

.. code-block:: bash

    python main.py

This will start the server and you can access the VisualML web interface by navigating to `http://127.0.0.1:5000/` in your web browser.

You can append the `--debug` flag to the command to run the server in debug mode

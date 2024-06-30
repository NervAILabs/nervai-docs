============================
VisualML Server Architecture
============================

The VisualML server is a Flask web server that serves the GUI and acts as the middleware between the GUI and the backend. The server provides a RESTful API that allows the GUI to interact with the backend and perform various operations, such as creating and managing machine learning pipelines.

.. graphviz:: /images/uml/classes_vml_server.dot

---------------------
Database Schema
---------------------

The server uses a file-based database to store information about the pipelines, including the pipeline configuration, the training data, and the trained models. The server also provides functionality to save and load pipelines from disk, allowing users to persist their work across sessions. This section explains the database schema to help you understand how the data is stored and how the server interacts with the database.

.. image:: /images/uml/database_schema.png
   :alt: Entity Relationship Diagram
   :width: 100%
   :align: center


---------------------
RESTful API
---------------------

The server provides a RESTful API that allows the GUI to interact with the backend. The API docs can be accessed at `/api/docs` endpoint when the server is running. This page shows a Swagger UI interface that allows users to explore and interact with the API endpoints.

---------------------
The User Interface
---------------------

The UI is build with vanilla JavaScript using custom web components derived from the Material Web Components library. The UI is designed to be simple and intuitive, allowing users to easily create and manage machine learning pipelines. The UI communicates with the server using the RESTful API to perform various operations, such as creating pipelines, training models, and evaluating models.

.. warning::
    In the future, the UI will be separated from the server, and the server will be used as a backend API server. The UI will be moved to a separate repository and will be developed as a standalone project.
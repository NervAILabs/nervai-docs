================================
Tracking with MLFlow
================================

MLflow is an open source platform for managing the end-to-end machine learning lifecycle. It tackles three primary functions:

- Tracking experiments to record and compare parameters and results ([MLflow Tracking](https://mlflow.org/docs/latest/tracking.html)).
- Packaging ML code in a reusable, reproducible form in order to share with other data scientists or transfer to production ([MLflow Projects](https://mlflow.org/docs/latest/projects.html)).
- Managing and deploying models from a variety of ML libraries to a variety of model serving and inference platforms ([MLflow Models](https://mlflow.org/docs/latest/models.html)).

.. note::
    MindGarage hosts a local MLFlow server for our internal use. You can use it by setting the tracking URI in your experiments to: [`http://mindgarage07.cs.uni-kl.de:8001`](http://mindgarage07.cs.uni-kl.de:8001).


-------------------------------------
Getting Started with MLFlow Tracking
-------------------------------------

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Prerequisites
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


In order to use MLFlow Tracking, you need to install the MLFlow Python package:

.. code-block:: bash

    pip install mlflow


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Signing in to the Tracking Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To sign in to the tracking server, you need to set the tracking URI to the server's URL. You can do this by calling the `mlflow.set_tracking_uri()` function:

.. code-block:: python

    mlflow.set_tracking_uri("http://mindgarage07.cs.uni-kl.de:8001")

.. warning::
    The tracking server is currently publicly accessible to anyone, which means anyone can see your experiments. We are working on a solution to this problem. Meanwhile, please do not log any sensitive information to the tracking server.

To learn more about signing into the tracking server, please refer to the [official documentation](https://mlflow.org/docs/latest/tracking/server.html#logging-to-a-tracking-server).


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Starting an Experiment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To start an experiment, you need to call the `mlflow.start_run()` function. This function returns a `Run` object, which you can use to log metrics, parameters, artifacts, etc. to the tracking server.

.. code-block:: python

    mlflow.set_experiment("My Experiment")
    with mlflow.start_run():
        # Your code here

The experiment name is used to identify the experiment in the tracking server. If the experiment does not exist, it will be created automatically. If you do not specify an experiment name, the default experiment will be used. See [this document](https://mlflow.org/docs/latest/tracking/tracking-api.html#organizing-runs-in-experiments) to learn more about organizing runs and experiments.


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Logging Metrics, Parameters, and Artifacts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To log metrics, parameters, and artifacts, you need to use the `Run` object returned by `mlflow.start_run()`. For example, to log a metric, you can use the `Run.log_metric()` function:


.. code-block:: python

    with mlflow.start_run():
        # Log a metric
        mlflow.log_metric("train_loss", 0.01)

        # Log a parameter
        mlflow.log_param("batch_size", 4)

        # Log an artifact (output file)
        with open("output.txt", "w") as f:
            f.write("Hello world!")
        mlflow.log_artifact("output.txt")

        # Log a model
        mlflow.pytorch.log_model(net, "model")

To log the entire configuration, you can use the `Run.log_params()` function:

.. code-block:: python

    with mlflow.start_run():
        mlflow.log_params({k: v for k, v in cfg.items()})

For more information on logging, please refer to the [official documentation](https://mlflow.org/docs/latest/tracking.html#tracking-runs).

-------------------------------------
Advanced Usage
-------------------------------------

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Using MLflow Tracking with MMPose
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are working with MMPose, you can use MMEngine's [`MLflowVisBackend`](https://github.com/open-mmlab/mmengine/blob/4a50213c6954d42536faa8b69b48bb6dd8f32f4f/mmengine/visualization/vis_backend.py#L638) to upload your experiments to the tracking server. To do this, you need to add the following in your config file:

.. code-block:: python

    vis_backends = [
        dict(type='LocalVisBackend'),
        dict(type='MLflowVisBackend',
            exp_name=EXP_NAME, # Optional
            run_name=RUN_NAME, # Optional
            tracking_uri=MINDGARAGE_MLFLOW_TRACKING_URI),
    ]
    visualizer = dict(
        type='PoseLocalVisualizer', vis_backends=vis_backends, name='visualizer')


We recommend setting the `exp_name` to the name of your config file, and the `run_name` to the current timestamp. For example,

.. code-block:: python

    import time
    exp_name='rtmpose-m_8xb256-420e_coco-256x192',
    run_name=time.strftime("%Y%m%d_%H%M%S", time.localtime()),

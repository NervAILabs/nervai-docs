=======================
Building a Custom Model
=======================

NervAI Engine is designed to work with any PyTorch model. We provide a :doc:`graphical model builder <../ui/model-building/index>` that allows you to build different types of models by connecting the available components (backbones, heads, losses, etc.). However, if you have a custom model that is not supported by the graphical model builder, you can still use NervAI Engine to visualize the model's architecture and keep track of its training process.

To use a custom model with NervAI Engine, you need to register the model with NervAI Engine's model registry. The model registry is a dictionary that maps model names to their corresponding classes. You can register your custom model using the ``@MODELS.register`` decorator.

.. code-block:: python

    from vml_sdk.registry import MODELS

    @MODELS.register_module()
    class MyModel(torch.nn.Module):
        def __init__(self, input_dim, output_dim):
            super(MyModel, self).__init__()
            self.fc = torch.nn.Linear(input_dim, output_dim)

        def forward(self, x):
            return self.fc(x)

Once a model is registered, NervAI Engine model can instantiate it from the configuration file using the model name.

.. code-block:: python

    model=dict(
        type='MyModel',
        input_dim=10,
        output_dim=1,
        # other model parameters
    )
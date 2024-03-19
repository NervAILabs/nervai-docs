# Metinor: A Neural Network Framework

Welcome to Metinor, your one-stop framework for neural network development, optimization, and visualization. Metinor is built on top of [PyTorch](https://pytorch.org/) and [PyTorch Lightning](https://lightning.ai/), leveraging their flexibility and ease-of-use.

The name "Metinor" is a fusion of "[Metis](https://en.wikipedia.org/wiki/Metis_(mythology))," the Greek Titaness of wisdom, and "[Valinor](https://en.wikipedia.org/wiki/Valinor)," the undying lands in J.R.R. Tolkien's literary universe where eternal wisdom and beauty prevail. Metinor aims to be the wise and enduring sanctuary for all your neural network needs, offering a suite of powerful tools and capabilities.

## Features

Metinor is an extensible framework that allows you to easily develop, visualize, and optimize neural networks. It offers the following features:

- A modular, object-oriented design that allows you to easily extend the framework with your own modules.
- A powerful visualization tool that allows you to visualize the structure of your neural network.
- A set of optimization algorithms that allow you to prune, quantize, and compress your neural network.

## Installation

To install Metinor, follow these steps:

1. Clone the repository to your local machine.
2. Create a new virtual environment using `python -m venv venv` and activate it.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Install OpenMMLab packages using `mim install -r requirements-mim.txt`.
5. Install MMPose using `pip install "mmpose==1.1.0"`
6. Install the package using `pip install .`.

## Development

To contribute to Metinor, follow these steps:

1. Clone the repository to your local machine.
2. Create a new virtual environment using `python -m venv venv` and activate it.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Install OpenMMLab packages using `mim install -r requirements-mim.txt`.
5. Install MMPose using `pip install "mmpose==1.1.0"`
6. Install the development dependencies using `pip install -r requirements-dev.txt`.
7. Install the package using `pip install -e .`.

### Unit Tests

To run the unit tests, run `pytest` in the root directory of the repository.

## Credits

Metinor is based on several open-source projects, including:

- [shrinkbench](https://github.com/JJGO/shrinkbench)
- [torchview](https://github.com/mert-kurttutan/torchview)
- [torchstat](https://github.com/Swall0w/torchstat)
- [torchprofile](https://github.com/zhijian-liu/torchprofile)


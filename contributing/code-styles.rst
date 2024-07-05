=================================
Code Styles
=================================

This document outlines the code styles and conventions used in the VisualML project. Following these guidelines will help maintain consistency across the codebase and make it easier for developers to read and understand the code.

Python Code Style
-----------------

The VisualML project follows the `PEP 8`_ style guide for Python code. This includes the following conventions:

- Use 4 spaces for indentation.
- Limit lines to 79 characters.
- Use `snake_case` for variable and function names.
- Use `CamelCase` for class names.
- Use `UPPER_CASE` for constants.
- Use spaces around operators and after commas.
- Use docstrings to document functions, classes, and modules.
- Use type hints for function arguments and return values.

.. _PEP 8: https://www.python.org/dev/peps/pep-0008/

We recommend using the following tools to ensure that your code follows the PEP 8 style guide:

- `isort`_: A tool that sorts and organizes your import statements according to PEP 8 guidelines.
- `Black`_: An opinionated code formatter that automatically formats your code to follow the PEP 8 style guide.
- `Flake8`_: A tool that checks your code for PEP 8 compliance and other code quality issues.
  
.. _isort: https://pycqa.github.io/isort/
.. _Black: https://black.readthedocs.io/en/stable/
.. _Flake8: https://flake8.pycqa.org/en/latest/

Before submitting a pull request, make sure to run these tools on your code to ensure that it follows the PEP 8 style guide.

.. code-block:: bash

    # Install isort, Black, and Flake8
    pip install isort black flake8

    # Run isort to organize import statements
    isort .

    # Run Black to format your code
    black .

    # Run Flake8 to check your code for PEP 8 compliance
    flake8 .

You should replace the `.` in the commands above with the path to the directory or file you want to check. You can also configure your code editor to run these tools automatically when you save a file. This will help you catch style violations early and ensure that your code follows the PEP 8 style guide.

JavaScript Code Style
---------------------

The VisualML project follows the `Airbnb JavaScript Style Guide`_ for JavaScript code. This includes the following conventions:

- Use 2 spaces for indentation.
- Limit lines to 100 characters.
- Use `camelCase` for variable and function names.
- Use `PascalCase` for class names.
- Use `UPPER_CASE` for constants.
- Use single quotes for strings.
- Use `===` for equality comparisons.
- Use `/** ... */` for multi-line comments.
- Use `//` for single-line comments.


.. _Airbnb JavaScript Style Guide: https://github.com/airbnb/javascript

We recommend using the following tools to ensure that your JavaScript code follows the Airbnb JavaScript Style Guide:

- `Prettier`_: An opinionated code formatter that automatically formats your code to follow the Airbnb JavaScript Style Guide.
- `ESLint`_: A tool that checks your code for JavaScript syntax errors and style issues.

.. _Prettier: https://prettier.io/
.. _ESLint: https://eslint.org/
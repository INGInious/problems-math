Installation and configuration
==============================

Dependencies setup
------------------

The plugin math needs :

- INGInious 0.8
- sympy 1.13.3
- antlr4-python3-runtime 4.11.1

Installation
------------

On Linux use :

.. code-block:: bash

    # pip3 install git+https://github.com/UCL-INGI/INGInious-problems-math

You also have to add the following plugin entry in your ``configuration.yaml`` file:

.. code-block:: yaml

    plugins:
        - plugin_module: "inginious_problems_math"


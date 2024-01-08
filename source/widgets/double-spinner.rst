===============
DoubleSpinner
===============

A specialized input box designed for entering floating-point (decimal) numbers. It allows users to adjust and input numeric values with decimal precision using a spinning mechanism. You can set a range for the values, define the step size for increments or decrements, and control the number of decimal places displayed, making it ideal for precise numeric input.

.. code-block:: lua

  local dock = DoubleSpinner()

Properties
***************

.. function:: setOnValueChange(callback)
  :noindex:

  The function executed when the value changes

  :params: ``self`` and ``value``

.. function:: setRange(start, end)
  
  Sets the ``minimum`` and ``maximum`` values for the widget

.. function:: setValue(value)
  
  Sets the value displayed on the widget

.. function:: getValue()
  :noindex:
  
  Returns the current value

.. function:: setPrefix(prefix)
  
  Set the prefix of the spinner widget

.. function:: setSuffix(suffix)
  
  Set the suffix of the spinner widget
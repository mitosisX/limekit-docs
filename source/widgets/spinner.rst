Spinner
===========

A widget that allows users to input integer values within a specified range. It provides a convenient interface for users to select numbers by either typing directly into the box or by using up and down arrow buttons to increase or decrease the value

.. code-block:: lua

  local dock = Spinner()

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

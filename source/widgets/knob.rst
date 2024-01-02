Knob
===========

A circular input control that allows users to interact by rotating it, usually to select numeric values within a defined range. It's commonly used for adjusting settings like volume, brightness, or any other parameter that can be controlled by rotating a knob. The circular design of the widget provides a visually intuitive way for users to modify values in an application


.. code-block:: lua

  local knob = Knob()

Properties
***************

.. function:: setOnValueChanged(callback)

  The function executed when the button is clicked

  :params: ``self`` and ``value``

.. function:: setRange(text)
  
  Sets the ``minimum`` and ``maximum`` values for the widget

.. function:: setValue(value)
  
  Sets current value for the widget

.. function:: setMinValue(value)
  
  Sets the minimum value for the widget

.. function:: setMaxValue(value)
  
  Sets the maximum value for the widget

.. function:: getValue()
  :noindex:
  
  Get current value

.. function:: setIndicators(enable: bool)
  
  Set whether or not markers are visible on the widget

.. function:: isIndicatorVisible()
  
  Check if markers are visible or not
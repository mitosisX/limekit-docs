ProgressBar
=============

A visual widget that shows the progress of a task or an operation. It appears as a bar that fills up gradually, representing the completion status of a process.

.. code-block:: lua

  local progress = ProgressBar()

Properties
***************

.. function:: setRange(start, end)
  :noindex:

  Sets the progress range

.. function:: setValue(value)

  Sets the current value

.. function:: getValue()

  Returns the current value

.. function:: setOrientation(orientation)

  Sets the orientation: ``horizontal`` or ``vertical``

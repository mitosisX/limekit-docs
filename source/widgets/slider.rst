Slider
===========

A widget that lets users select a value from a range by sliding a handle or by clicking at specific points along a track allowing them to set a value according to the position of the handle.

.. code-block:: lua

  local slider = Slider()

Properties
***************

.. function:: setRange(start, end)
  :noindex:

  Sets the slider's range

.. function:: setValue(value)
  :noindex:

  Sets the current value

.. function:: getValue()

  Returns the current value

.. function:: setOrientation(orientation)

  Sets the orientation: ``horizontal`` or ``vertical``

.. function:: setTickPosition(position)

  Sets the position of tick marks on a slider

  :mod:`Positions`: ``none``, ``above``, ``left``, ``below``, ``right`` and ``bothsides``
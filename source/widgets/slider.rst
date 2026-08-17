Slider
###########

A handle dragged along a track to pick a number. Good for volume, brightness,
and anything where the rough position matters more than the exact figure.

.. code-block:: lua

  local ui = require("limekit.ui")

  local volume = ui.Slider()
  volume:setRange(0, 100)
  volume:setValue(50)

Sliders are horizontal unless you say otherwise.

Properties
***************

.. function:: setValue(value) / getValue()
  :no-index:

  The current number.

.. function:: setRange(start, end_)
  :no-index:

  The lowest and highest values.

.. function:: setOrientation(orientation) / getOrientation()
  :no-index:

  ``horizontal`` or ``vertical``.

  .. code-block:: lua

     volume:setOrientation("vertical")

.. function:: setTickPosition(position) / getTickPosition()
  :no-index:

  Where the tick marks are drawn: ``none``, ``above``, ``below``, ``left``,
  ``right`` or ``bothsides``.

.. function:: setOnValueChange(callback)
  :no-index:

  Runs as the handle moves. The handler receives the slider and the new value.

  .. code-block:: lua

     volume:setOnValueChange(function(sender, value)
         label:setText("Volume: " .. value)
     end)

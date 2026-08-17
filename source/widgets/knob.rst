Knob
###########

A dial the user turns to pick a value. The same idea as a
:doc:`Slider </widgets/slider>` in a round shape, which suits audio and
instrument-style interfaces.

.. code-block:: lua

  local ui = require("limekit.ui")

  local tone = ui.Knob()
  tone:setRange(0, 10)
  tone:setValue(5)
  tone:setNotchesVisible(true)

Properties
***************

.. function:: setValue(value) / getValue()
  :no-index:

  The current value.

.. function:: setRange(minimum, maximum)
  :no-index:

  The lowest and highest values.

.. function:: setMinValue(minimum) / setMaxValue(maximum)
  :no-index:

  The ends of the range individually.

.. function:: setNotchesVisible(visible) / isNotchesVisible()
  :no-index:

  Whether tick marks are drawn around the dial.

.. function:: setOnValueChanged(callback)
  :no-index:

  Runs as the dial is turned.

  .. code-block:: lua

     tone:setOnValueChanged(function(sender, value)
         print("tone: " .. value)
     end)

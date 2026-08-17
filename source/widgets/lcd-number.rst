LCDNumber
############

Displays a number in the style of a calculator or digital clock.

.. code-block:: lua

  local ui = require("limekit.ui")

  local counter = ui.LCDNumber()
  counter:setDigitCount(6)
  counter:setValue(1234)

Properties
***************

.. function:: setValue(value) / getValue()
  :no-index:

  The number shown.

  .. note::

     In 1.x this method was misspelled ``setValuee`` and could only ever raise
     an error. ``setValue`` is the working replacement.

.. function:: setDigitCount(count) / getDigitCount()
  :no-index:

  How many digits the display has room for.

.. function:: setSegmentStyle(style) / getSegmentStyle()
  :no-index:

  How the digits are drawn: ``filled``, ``flat`` or ``outline``.

.. function:: setMatProperty(class_)
  :no-index:

  Applies a Material Design styling class, when a material theme is active.

Example: a clock
*******************

.. code-block:: lua
  :linenos:

  local ui  = require("limekit.ui")
  local sys = require("limekit.sys")

  local clock = ui.LCDNumber()
  clock:setDigitCount(8)

  local ticker = sys.Timer()
  ticker:setInterval(1000)
  ticker:setOnTimeout(function()
      clock:setValue(os.date("%H%M%S"))
  end)
  ticker:start()

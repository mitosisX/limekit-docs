TimePicker
#############

A field for choosing a time of day.

.. code-block:: lua

  local ui = require("limekit.ui")

  local alarm = ui.TimePicker()
  alarm:setTime(7, 30)

Properties
***************

.. function:: setTime(hour, minute, second)
  :no-index:

  Sets the time shown. ``second`` is optional and defaults to 0.

  .. note::

     1.x had a ``setDate(year, month, day)`` method here, which fed a date into
     a widget that only holds a time and never worked. ``setTime`` replaces it.

.. function:: getTime()
  :no-index:

  The time currently shown.

.. function:: setOnTimePicked(callback)
  :no-index:

  Runs when the time changes.

  .. code-block:: lua

     alarm:setOnTimePicked(function(sender)
         print("alarm set for " .. tostring(sender:getTime()))
     end)

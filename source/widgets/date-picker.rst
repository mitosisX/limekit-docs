DatePicker
#############

A compact field for choosing a date, with a drop-down calendar. Use a
:doc:`Calendar </widgets/calendar>` when you want the whole month on screen.

.. code-block:: lua

  local ui = require("limekit.ui")

  local due = ui.DatePicker()
  due:setDate(2026, 8, 17)

Properties
***************

.. function:: setDate(year, month, day)
  :no-index:

  Sets the date shown.

  .. note::

     In 1.x this method also took ``hour`` and ``minutes``, which were never
     displayed -- and the call raised an error every time it was made. A date
     picker holds a date, so those arguments are gone. For a time, use a
     :doc:`TimePicker </widgets/time-picker>`.

.. function:: getDate()
  :no-index:

  The date currently shown.

.. function:: setOnDatePick(callback)
  :no-index:

  Runs when the date changes.

  .. code-block:: lua

     due:setOnDatePick(function(sender)
         print("due " .. tostring(sender:getDate()))
     end)

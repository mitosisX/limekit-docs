Calendar
###########

A full month view the user can page through and pick a day from. When you only
need a compact field, use a :doc:`DatePicker </widgets/date-picker>`.

.. code-block:: lua

  local ui = require("limekit.ui")

  local calendar = ui.Calendar()
  calendar:setDate(2026, 8, 17)

  calendar:setOnDatePicked(function(sender)
      print(sender:getDate())
  end)

Properties
***************

.. function:: setDate(year, month, day)
  :no-index:

  Selects a date.

.. function:: getDate()
  :no-index:

  The selected date.

.. function:: setGridVisible(visible) / isGridVisible()
  :no-index:

  Whether grid lines are drawn between the days.

.. function:: setOnDatePicked(callback)
  :no-index:

  Runs when the user picks a date.

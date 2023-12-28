DatePicker
============

A widget in PyQt specifically designed for editing dates. It provides a user-friendly interface for selecting dates through a calendar or by manually inputting the date. It's handy for tasks requiring date selection or entry, ensuring users can easily input or modify dates in an application

.. code-block:: lua

  local date = DatePicker()

Methods
***************

.. function:: setOnDatePick(callback)
  :noindex:

  The function executed when the button is clicked

  :params: self and date

.. function:: setDate(self, year, month, day, hour: optional, minutes: optional)
  
  Sets the date

.. function:: getDate()
  
  Returns the date in year-month-day format
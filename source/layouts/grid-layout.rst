============
GridLayout
============

This layout is like a grid or table where you can neatly arrange widgets in rows and columns. It's a layout manager that helps you organize various elements within a window or interface. You can specify where each widget should go in the grid, and the layout ensures they are positioned accordingly. It's great for creating structured interfaces where widgets need to be aligned in rows and columns, similar to organizing information in a table.

.. code-block:: lua

  local layout = GridLayout()

Properties
***************

.. function:: addChild(widget, row, column, rowSpan: optional, columnSpan: optional)
  
  Adds a widget to the layout on a specified row (``x position``) and column (``y position``). The ``rowSpan`` and ``columnSpan`` are optional but allow a widget to span multiple rows or columns.

.. function:: addLayout(layout, row, column, rowSpan: optional, columnSpan: optional)

  Similar to the above property, now only for layouts.

.. function:: getChildAt(row, column)

  Retrieves a widget at a specified row and column

.. function:: setColumnStretch(column, stretch)

  This method allows you to control how the columns of the layout expand or contract when the parent widget is resized.

.. function:: setMargins(left, top,right,bottom)

  Sets the margins of the layout
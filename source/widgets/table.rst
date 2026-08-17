Table
###########

A grid of rows and columns, for spreadsheet-like data.

.. code-block:: lua
  :linenos:

  local ui = require("limekit.ui")

  local sheet = ui.Table(3, 2)
  sheet:setColumnHeaders({ "Name", "Score" })

  sheet:setCellText(1, 1, "Ada")
  sheet:setCellText(1, 2, "98")
  sheet:setCellText(2, 1, "Grace")
  sheet:setCellText(2, 2, "95")

.. important::

  **Rows and columns start at 1.** The top-left cell is ``(1, 1)``.

  This changed in 2.0 -- the 1.x Table counted from 0. Passing ``0`` now raises
  an error rather than quietly touching the wrong cell.

Size
***************

.. function:: ui.Table(rows, columns)
  :no-index:

  Creates a table of a given size. Both default to 0.

.. function:: setRowCount(rows) / getRowCount()
  :no-index:

  How many rows the table has.

.. function:: setColumnCount(columns) / getColumnCount()
  :no-index:

  How many columns the table has.

.. function:: addRow()
  :no-index:

  Appends an empty row to the bottom.

.. function:: insertRowAt(row) / removeRowAt(row)
  :no-index:

  Inserts or removes a row at a position.

.. function:: insertColumnAt(column) / removeColumnAt(column)
  :no-index:

  Inserts or removes a column at a position.

.. function:: clear()
  :no-index:

  Removes everything, headers included.

.. function:: clearContent()
  :no-index:

  Empties the cells but keeps the headers and the grid size.

Headers
***************

.. function:: setColumnHeaders(headers)
  :no-index:

  The labels along the top, from a table of strings.

.. function:: setRowHeaders(headers)
  :no-index:

  The labels down the side.

.. function:: getColumnHeaderText(column)
  :no-index:

  The label of one column.

.. function:: setColumnWidth(column, width)
  :no-index:

  How wide a column is, in pixels.

Cells
***************

.. function:: setCellText(row, column, text)
  :no-index:

  Puts text in a cell.

.. function:: getCellItem(row, column)
  :no-index:

  The :doc:`TableItem </widget-items/table-item>` in a cell, which is how you
  colour an individual cell.

  .. code-block:: lua

     local cell = sheet:getCellItem(1, 2)
     cell:setBackgroundColour("#ffe08a")

.. function:: setCellChild(row, column, child)
  :no-index:

  Puts a whole widget in a cell -- a button, a checkbox, a combo box.

  .. code-block:: lua

     sheet:setCellChild(1, 2, ui.CheckBox("Done"))

.. function:: getCellChild(row, column)
  :no-index:

  The widget in a cell, if one was set.

.. function:: setCellsEditable(editable)
  :no-index:

  Whether the user may type into cells.

Selection
***************

.. function:: setCurrentCell(row, column)
  :no-index:

  Selects a cell.

.. function:: getCurrentRow() / getCurrentColumn()
  :no-index:

  Where the selection currently is.

.. function:: getCurrentItem()
  :no-index:

  The selected cell's item.

.. function:: setSelectionBehavior(behavior)
  :no-index:

  Whether clicking selects a single cell, a whole row, or a whole column.

Appearance
***************

.. function:: setShowGrid(show) / isShowGrid()
  :no-index:

  Whether the grid lines are drawn.

.. function:: setAlternatingRowColors(alternate) / isAlternatingRowColors()
  :no-index:

  Shades every other row, which makes wide tables much easier to read.

.. function:: setSortingEnabled(enabled) / isSortingEnabled()
  :no-index:

  Lets the user sort by clicking a column header.

Events
***************

.. function:: setOnCellClick(callback)
  :no-index:

  Runs when a cell is clicked.

.. function:: setOnCellDoubleClick(callback)
  :no-index:

  Runs when a cell is double-clicked.

.. function:: setOnCellChange(callback)
  :no-index:

  Runs when a cell's contents change.

  .. code-block:: lua

     sheet:setOnCellChange(function(sender)
         print("changed row " .. sender:getCurrentRow())
     end)

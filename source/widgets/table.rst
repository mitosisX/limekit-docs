Table
===========

A widget where users can view, edit, and interact with data presented in a grid-like format. It allows developers to populate the table with data, set headers for rows and columns, and enable users to edit cell contents. This widget offers functionalities to manage and manipulate tabular data, including sorting, selecting cells, adding or removing rows/columns dynamically. It's a powerful tool for displaying structured data or creating spreadsheet-like interfaces.

.. code-block:: lua

  local table = Table(rows, columns) -- optional parameters; specfies number of rows and columns

.. important::

  Row and column indexing starts at :mod:`0`

Properties
***************

.. function:: setOnCellEditFinished(callback)

  Executed when user finishes editing a particular cell

.. function:: setOnCellClicked(callback)

  Executed when a cell was clicked

.. function:: setOnCellDoubleClicked(callback)

  Executed when a cell gets double clicked

.. function:: setOnCellSelection(callback)

  Executed when a cell is selected

  :params: self, row, column

.. function:: addData(row, column, text)

  Adds text to row and column
  
.. function:: setImageData(image, text, row, column)

  Sets an image and text on specified row and column

.. function:: setColumnHeaders(columns: table)

  Sets columns for the widget,ie, ``{'Name', 'Age', 'Location', ...}``

.. function:: setRowHeaders(headers: table)

  Same as above property

.. function:: getCurrentColumn()

  Returns the current column

.. function:: getCurrentRow()

  Returns the current row

.. function:: setMaxColumns(columns)

  Sets the maximum columns for the widget

.. function:: setMaxRows(rows)

  Sets the maximum rows for the widget

.. function:: setColumnHeaderToolTip(column: number)

  Sets the tooltip for a particular header index

.. function:: getColumnHeaderText(column: number)

  Returns the column header text

.. function:: getColumnsCount()

  Returns total columns in the widget

.. function:: getRowsCount()

  Returns total rows in the widget

.. function:: setGridVisible(visibility)
  :noindex:

  Sets grid-lines visibility for the widget

.. function:: setRowLabelsVisible(visibility)

  Sets the visibility for row labels; ``1,2,3,4,5`` on the left hand side

.. function:: setCellChild(row, column, child)

  Sets a widget on a particular row and column

.. function:: setAutoColumnResize()

  Sets columns to automatically adjust to content

.. function:: setAutoRowResize()

  Sets rows to automatically adjust to content

.. function:: setColumnFitsContent(column)

  Manually adjust a particular column

.. function:: deleteRow(row)

  Deletes a particular row

.. function:: setCellsEditable(editable: bool)

  Enables or disables cell editing

.. function:: setAltRowColors(altcolors: bool)

  Sets alternating colors

.. function:: setColumnSorting(enable: bool)

  Eanbles or disables column header sorting

.. function:: clear()

  Clears all content, including the headers

.. function:: clearContent()

  Clears only values in the cells, excluding the headers and row labels

.. function:: findDataItem(text)

  Searches for particular text in the widget

.. function:: insertColumnAt(column)

  Inserts a new column on a specified column index

.. function:: insertRowAt(row)

  Inserts a new row on a specified row index

.. function:: removeColumnAt(column)

  Removes a column at a particular column index

.. function:: removeRowAt(row)

  Removes a row at a particular row index

.. function:: getItemAt(row, column)

  Returns a :mod:`TableItem` at a particular row and column

.. function:: getSelectedCells()

  Returns all selected cells

.. function:: getSelectedCell()

  Returns selected cell

.. function:: setSpan(row, column, rowSpan, columnSpan)

  Merges cells toegther, allowing them to span multiple rows and columns within the table. Useful for creating cells that cover a large area within the table layout

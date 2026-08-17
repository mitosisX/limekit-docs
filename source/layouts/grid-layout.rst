GridLayout
#############

Arranges widgets in rows and columns. Calculators, keypads and dense forms are
the natural fit.

.. code-block:: lua
  :linenos:

  local ui = require("limekit.ui")

  local grid = ui.GridLayout()
  grid:addChild(ui.Button("7"), 1, 1)
  grid:addChild(ui.Button("8"), 1, 2)
  grid:addChild(ui.Button("9"), 1, 3)
  grid:addChild(ui.Button("4"), 2, 1)
  grid:addChild(ui.Button("5"), 2, 2)
  grid:addChild(ui.Button("6"), 2, 3)

.. important::

  **Rows and columns start at 1.** The top-left cell is ``(1, 1)``.

Properties
***************

.. function:: addChild(child, row, column, rowSpan, columnSpan)
  :no-index:

  Places a widget in a cell. ``rowSpan`` and ``columnSpan`` let it cover several
  cells and both default to 1.

  .. code-block:: lua

     -- a wide button across the bottom three columns
     grid:addChild(ui.Button("="), 3, 1, 1, 3)

.. function:: addLayout(layout, row, column, rowSpan, columnSpan)
  :no-index:

  Places a nested layout in a cell.

.. function:: getChildAt(row, column)
  :no-index:

  The widget in a cell.

.. function:: setRowStretch(row, stretch)
  :no-index:

  How much of the spare height a row takes compared with the others.

.. function:: setColumnStretch(column, stretch)
  :no-index:

  How much of the spare width a column takes.

  .. code-block:: lua

     -- second column grows, first stays as small as it can
     grid:setColumnStretch(1, 0)
     grid:setColumnStretch(2, 1)

.. seealso::

  :doc:`Layout Managers </layouts>` for the methods every layout shares.

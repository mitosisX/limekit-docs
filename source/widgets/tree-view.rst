TreeView
###########

A hierarchy of items that can be expanded and collapsed -- file browsers,
outlines, category trees.

A tree is built from :doc:`TreeViewItem </widget-items/tree-view-item>` objects.
Top-level items go on the tree; everything else goes on another item.

.. code-block:: lua
  :linenos:

  local ui = require("limekit.ui")

  local tree = ui.TreeView()
  tree:setHeaderLabels({ "Name", "Size" })

  local documents = ui.TreeViewItem({ "Documents", "" })
  documents:addChild(ui.TreeViewItem({ "report.pdf", "2 MB" }))
  documents:addChild(ui.TreeViewItem({ "notes.txt", "4 KB" }))

  tree:addTopItem(documents)
  documents:setExpanded(true)

.. note::

  The 1.x name ``TreeWidget`` still works and refers to this same widget.

Structure
***************

.. function:: addTopItem(item)
  :no-index:

  Adds a top-level item.

.. function:: getTopItemAt(index)
  :no-index:

  The top-level item at a position. **Positions start at 1.**

.. function:: getTopItemCount()
  :no-index:

  How many top-level items the tree has.

.. function:: clear()
  :no-index:

  Removes everything.

Headers and columns
**********************

.. function:: setHeaderLabels(labels)
  :no-index:

  The column headings, from a table of strings. The number of labels sets the
  number of columns.

.. function:: setHeaderHidden(hidden) / isHeaderHidden()
  :no-index:

  Hides the header row, which suits a simple one-column tree.

.. function:: setColumnWidth(column, width)
  :no-index:

  How wide a column is, in pixels.

Expanding
***************

.. function:: expandAll()
  :no-index:

  Opens every branch.

.. function:: collapseAll()
  :no-index:

  Closes every branch.

Selection
***************

.. function:: getCurrentItem()
  :no-index:

  The selected item.

Events
***************

.. function:: setOnItemClick(callback)
  :no-index:

  Runs when an item is clicked. The handler receives the tree, the item, and
  the column that was clicked -- 1-based, so it can go straight into the
  item's ``getText``.

  .. code-block:: lua

     tree:setOnItemClick(function(sender, item, column)
         print(item:getText(column))
     end)

.. function:: setOnItemDoubleClick(callback)
  :no-index:

  Runs when an item is double-clicked.

  .. code-block:: lua

     tree:setOnItemDoubleClick(function(sender)
         local item = sender:getCurrentItem()
         print("opening " .. item:getText(1))
     end)

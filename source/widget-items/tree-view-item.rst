TreeViewItem
###############

A branch or leaf in a :doc:`TreeView </widgets/tree-view>`. Items hold other
items, which is how the hierarchy is built.

An item is created with a table of texts -- one per column of the tree.

.. code-block:: lua
  :linenos:

  local ui = require("limekit.ui")

  local tree = ui.TreeView()
  tree:setHeaderLabels({ "Name", "Size" })

  local folder = ui.TreeViewItem({ "Documents", "" })
  folder:addChild(ui.TreeViewItem({ "report.pdf", "2 MB" }))
  folder:addChild(ui.TreeViewItem({ "notes.txt", "4 KB" }))

  tree:addTopItem(folder)
  folder:setExpanded(true)

Structure
***************

.. function:: ui.TreeViewItem(texts)
  :no-index:

  Creates an item from a table of column texts.

.. function:: addChild(child)
  :no-index:

  Nests another item beneath this one.

.. function:: getChildAt(index)
  :no-index:

  The child at a position. **Positions start at 1.**

.. function:: getChildCount()
  :no-index:

  How many children this item has.

.. function:: getParent()
  :no-index:

  The item this one sits beneath, or nothing for a top-level item.

Contents
***************

.. function:: setText(column, text) / getText(column)
  :no-index:

  The text in one column of this item. **Columns start at 1.**

  .. code-block:: lua

     folder:setText(2, "12 MB")

.. function:: setIcon(column, icon)
  :no-index:

  An icon in one column.

.. function:: setExpanded(expanded) / isExpanded()
  :no-index:

  Whether this item's children are showing.

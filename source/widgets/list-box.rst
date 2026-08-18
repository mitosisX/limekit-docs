ListBox
###########

A scrollable list of items, all visible at once. Where a
:doc:`ComboBox </widgets/combo-box>` hides its options until clicked, a ListBox
shows them.

.. code-block:: lua

  local ui = require("limekit.ui")

  local tasks = ui.ListBox({ "Write docs", "Fix bug", "Ship release" })

Items
***************

.. function:: setItems(items)
  :no-index:

  Replaces the list with a table of strings.

.. function:: addImageItem(label, image)
  :no-index:

  Adds an item with an icon beside its text.

  .. code-block:: lua

     local res = require("limekit.res")
     tasks:addImageItem("Deploy", res.Resources.images("rocket.png"))

.. function:: insertItemAt(row, item)
  :no-index:

  Inserts an item at a position, pushing the rest down. **Rows start at 1.**

.. function:: removeItemAt(row)
  :no-index:

  Removes the item at a position.

.. function:: getItemAt(index)
  :no-index:

  The item at a position.

.. function:: getItemsCount()
  :no-index:

  How many items the list holds.

.. function:: clear()
  :no-index:

  Removes every item.

Selection
***************

.. function:: setCurrentRow(row) / getCurrentRow()
  :no-index:

  The selected row. **Rows start at 1.**

  .. code-block:: lua

     tasks:setCurrentRow(1)
     print(tasks:getItemAt(tasks:getCurrentRow()))

Events
***************

.. function:: setOnItemSelect(callback)
  :no-index:

  Runs when the selected item changes. The handler receives the list, the
  selected item's text, and its row -- 1-based, so it goes straight back into
  ``getItemAt``.

.. function:: setOnItemDoubleClick(callback)
  :no-index:

  Runs when an item is double-clicked -- the usual way to "open" something in a
  list. Receives the list, the item's text, and its 1-based row.

  .. code-block:: lua

     tasks:setOnItemDoubleClick(function(sender, text, row)
         openTask(text)
     end)

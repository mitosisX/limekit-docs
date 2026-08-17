ComboBox
###########

A drop-down list. Compact when closed, so it suits a choice between many
options where a set of :doc:`radio buttons </widgets/radio-button>` would take
too much room.

.. code-block:: lua

  local ui = require("limekit.ui")

  local country = ui.ComboBox({ "Malawi", "Kenya", "Ghana" })

Properties
***************

.. function:: setItems(items)
  :no-index:

  Replaces the list with a table of strings.

.. function:: getItemAt(index)
  :no-index:

  The item at a position. **Positions start at 1.**

  .. code-block:: lua

     print(country:getItemAt(1))   -- Malawi

.. function:: getText()
  :no-index:

  The currently selected item.

.. function:: clear()
  :no-index:

  Removes every item.

.. function:: setEditable(editable) / isEditable()
  :no-index:

  Lets the user type a value of their own instead of only picking from the list.

.. function:: setOnItemSelect(callback)
  :no-index:

  Runs when the selection changes. The handler receives the combo box and
  the selected position, 1-based.

  .. code-block:: lua

     country:setOnItemSelect(function(sender, index)
         print("selected " .. sender:getItemAt(index))
     end)

  .. note::

     When nothing is selected -- after ``clear()``, for instance -- the
     position is ``0``, which is out of range for every 1-based method.
     Check for it before passing it on.

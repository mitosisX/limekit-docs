TableItem
############

A single cell in a :doc:`Table </widgets/table>`. You mostly do not create these
yourself -- ``setCellText`` makes one for you. Reach for the item when you want
to colour an individual cell.

.. code-block:: lua
  :linenos:

  local ui = require("limekit.ui")

  local sheet = ui.Table(2, 2)
  sheet:setCellText(1, 1, "Overdue")

  local cell = sheet:getCellItem(1, 1)
  cell:setBackgroundColour("#ffdddd")
  cell:setTextColour("#a00000")

You can also build one up and place it yourself:

.. code-block:: lua

  local item = ui.TableItem("Paid")
  item:setBackgroundColour("#ddffdd")

Properties
***************

.. function:: setText(text) / getText()
  :no-index:

  The cell's contents.

.. function:: setBackgroundColour(colour)
  :no-index:

  The cell's background. Accepts a colour name, a hex string, or an
  ``{r, g, b}`` table.

.. function:: setTextColour(colour)
  :no-index:

  The colour of the text in the cell.

.. note::

  These two are spelled the British way, with ``-colour``. The widget-wide
  ``setBackgroundColor`` on :doc:`every other widget </widgets>` uses the
  American spelling.

FontComboBox
###############

A drop-down already filled with the fonts installed on the machine. Use it
instead of a :doc:`ComboBox </widgets/combo-box>` when the choice is a typeface.

.. code-block:: lua

  local ui = require("limekit.ui")

  local fonts = ui.FontComboBox()
  fonts:setOnItemSelect(function(sender)
      preview:setStyleSheet("font-family: '" .. sender:getText() .. "';")
  end)

Properties
***************

.. function:: getText()
  :no-index:

  The name of the selected font.

.. function:: setCurrentFont(font) / getCurrentFont()
  :no-index:

  The selected font.

.. function:: setCurrentIndex(index) / getCurrentIndex()
  :no-index:

  The selected position. **Positions start at 1.**

.. function:: setFont(name)
  :no-index:

  Selects a font by name.

.. function:: addItem(text)
  :no-index:

  Adds an extra entry to the list.

.. function:: addItems(items)
  :no-index:

  Adds several extra entries from a table.

.. function:: addImageItem(icon, text)
  :no-index:

  Adds an entry with an icon beside it.

.. function:: setOnItemSelect(callback)
  :no-index:

  Runs when a different font is chosen.

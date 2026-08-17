RadioButton
##############

One choice out of several. Radio buttons in the same container are mutually
exclusive -- ticking one unticks the rest.

.. code-block:: lua

  local ui = require("limekit.ui")

  local small  = ui.RadioButton("Small")
  local medium = ui.RadioButton("Medium")
  local large  = ui.RadioButton("Large")

  medium:setChecked(true)

.. note::

  Exclusivity is decided by which container the buttons share. If you need two
  independent groups in one place, put each in its own
  :doc:`GroupBox </widgets/group-box>` or
  :doc:`ButtonGroup </widgets/button-group>`.

Properties
***************

.. function:: setText(text) / getText()
  :no-index:

  The label beside the button.

.. function:: setChecked(checked) / isChecked()
  :no-index:

  Whether this option is the selected one.

.. function:: setIcon(path) / getIcon()
  :no-index:

  An icon shown alongside the label.

.. function:: setIconSize(size) / getIconSize()
  :no-index:

  The icon size, from a ``{width, height}`` pair.

.. function:: setOnClick(callback)
  :no-index:

  Runs when the button is chosen.

  .. code-block:: lua

     local function chooseSize(sender)
         print("size: " .. sender:getText())
     end

     small:setOnClick(chooseSize)
     medium:setOnClick(chooseSize)
     large:setOnClick(chooseSize)

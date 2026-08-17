ToolbarButton
################

A button on a :doc:`Toolbar </widgets/tool-bar>`.

.. code-block:: lua
  :linenos:

  local ui  = require("limekit.ui")
  local res = require("limekit.res")

  local save = ui.ToolbarButton("Save")
  save:setIcon(res.Resources.images("save.png"))
  save:setToolTip("Save the current document")
  save:setShortcut("Ctrl+S")
  save:setOnClick(function()
      saveDocument()
  end)

  toolbar:addButton(save)

.. important::

  Toolbar buttons are often shown as icons only, with no text. Always set a
  tooltip -- it is the only way a user finds out what an unfamiliar icon does.

Properties
***************

.. function:: setText(text) / getText()
  :no-index:

  The button's label.

.. function:: setIcon(path) / getIcon()
  :no-index:

  The button's icon.

.. function:: setShortcut(sequence) / getShortcut()
  :no-index:

  A keyboard shortcut such as ``"Ctrl+S"``.

.. function:: setToolTip(text) / getToolTip()
  :no-index:

  The tooltip shown on hover.

.. function:: setStatusTip(text) / getStatusTip()
  :no-index:

  Text shown in the :doc:`StatusBar </widgets/status-bar>` on hover.

.. function:: setEnabled(enabled) / isEnabled()
  :no-index:

  Whether the button can be pressed.

.. function:: setVisible(visible) / isVisible()
  :no-index:

  Whether the button appears.

.. function:: setSeparator(separator) / isSeparator()
  :no-index:

  Turns the button into a dividing line.

.. function:: setMenu(menu)
  :no-index:

  Attaches a :doc:`DropMenu </widgets/drop-menu>` that opens when the button is
  pressed.

Toggle buttons
***************

.. function:: setCheckable(checkable) / isCheckable()
  :no-index:

  Lets the button stay pressed, for a mode that is on or off.

.. function:: setChecked(checked) / isChecked()
  :no-index:

  The pressed state.

  .. note::

     In 1.x ``isChecked()`` raised an error every time it was called. It returns
     a boolean now.

.. function:: toggle()
  :no-index:

  Flips the pressed state.

Events
***************

.. function:: setOnClick(callback)
  :no-index:

  Runs when the button is pressed.

.. function:: trigger()
  :no-index:

  Presses the button from code.

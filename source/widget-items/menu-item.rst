MenuItem
###########

A single command in a :doc:`Menu </widgets/menu>`.

.. code-block:: lua
  :linenos:

  local ui = require("limekit.ui")

  local save = ui.MenuItem("Save")
  save:setShortcut("Ctrl+S")
  save:setOnClick(function()
      saveDocument()
  end)

  fileMenu:addMenuItem(save)

Properties
***************

.. function:: setText(text) / getText()
  :no-index:

  The command's label.

.. function:: setIcon(path) / getIcon()
  :no-index:

  An icon beside the label.

.. function:: setShortcut(sequence) / getShortcut()
  :no-index:

  A keyboard shortcut, written the usual way: ``"Ctrl+S"``, ``"Ctrl+Shift+N"``,
  ``"F5"``. The shortcut is shown next to the command in the menu.

.. function:: setEnabled(enabled) / isEnabled()
  :no-index:

  Whether the command can be chosen. Grey out what does not currently apply
  rather than removing it -- people learn where things are.

.. function:: setVisible(visible) / isVisible()
  :no-index:

  Whether the command appears at all.

.. function:: setToolTip(text) / getToolTip()
  :no-index:

  The tooltip shown on hover.

.. function:: setStatusTip(text) / getStatusTip()
  :no-index:

  Text shown in the :doc:`StatusBar </widgets/status-bar>` while the command is
  highlighted.

.. function:: setSeparator(separator) / isSeparator()
  :no-index:

  Turns the item into a dividing line.

Checkable commands
*********************

.. function:: setCheckable(checkable) / isCheckable()
  :no-index:

  Gives the command a tick, for options that are on or off.

.. function:: setChecked(checked) / isChecked()
  :no-index:

  The tick state.

  .. code-block:: lua

     local wrap = ui.MenuItem("Word wrap")
     wrap:setCheckable(true)
     wrap:setChecked(true)
     wrap:setOnClick(function(sender)
         editor:setWordWrap(sender:isChecked())
     end)

.. function:: toggle()
  :no-index:

  Flips the tick.

Events
***************

.. function:: setOnClick(callback)
  :no-index:

  Runs when the command is chosen.

.. function:: trigger()
  :no-index:

  Runs the command from code, as though the user had chosen it.

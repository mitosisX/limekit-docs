Toolbar
###########

A row of buttons for the commands people use most. Toolbars hold
:doc:`ToolbarButtons </widget-items/toolbar-item>`, and can hold ordinary
widgets too.

.. code-block:: lua
  :linenos:

  local ui  = require("limekit.ui")
  local res = require("limekit.res")

  local toolbar = ui.Toolbar("Main")

  local save = ui.ToolbarButton("Save")
  save:setIcon(res.Resources.images("save.png"))
  save:setShortcut("Ctrl+S")
  save:setOnClick(function()
      saveDocument()
  end)

  toolbar:addButton(save)
  toolbar:addSeparator()
  toolbar:addChild(ui.LineEdit())

  window:addToolbar(toolbar, "top")

Contents
***************

.. function:: addButton(button)
  :no-index:

  Adds a :doc:`ToolbarButton </widget-items/toolbar-item>`.

.. function:: addChild(child)
  :no-index:

  Adds an ordinary widget -- a search box, a combo box, a progress bar.

.. function:: addSeparator()
  :no-index:

  Adds a dividing line between groups of buttons.

Appearance
***************

.. function:: setToolButtonStyle(style) / getToolButtonStyle()
  :no-index:

  How buttons are drawn: ``icononly``, ``textonly``, ``textbesideicon``,
  ``textundericon`` or ``followstyle``.

  .. code-block:: lua

     toolbar:setToolButtonStyle("textundericon")

.. function:: setIconSize(size) / getIconSize()
  :no-index:

  The button icon size, from a ``{width, height}`` pair.

.. function:: setMovable(movable) / isMovable()
  :no-index:

  Lets the user drag the toolbar to a different edge.

.. function:: setFloatable(floatable) / isFloatable()
  :no-index:

  Lets the user pull the toolbar off into its own small window.

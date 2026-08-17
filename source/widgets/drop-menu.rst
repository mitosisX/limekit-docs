DropMenu
###########

A :doc:`Menu </widgets/menu>` intended to drop down from a button rather than
sit on a menubar. It has the same methods as Menu.

.. code-block:: lua
  :linenos:

  local ui = require("limekit.ui")

  local actions = ui.DropMenu()
  actions:addMenuItem(ui.MenuItem("Duplicate"))
  actions:addMenuItem(ui.MenuItem("Rename"))
  actions:addSeparator()
  actions:addMenuItem(ui.MenuItem("Delete"))

  local more = ui.Button("More")
  more:setMenu(actions)

Contents
***************

.. function:: addMenuItem(item)
  :no-index:

  Adds a command.

.. function:: addMenu(menu)
  :no-index:

  Adds a submenu.

.. function:: addSeparator()
  :no-index:

  Adds a dividing line.

Appearance
***************

.. function:: setTitle(text) / getTitle()
  :no-index:

  The menu's name.

.. function:: setIcon(path) / getIcon()
  :no-index:

  An icon beside the name.

Events
***************

.. function:: setOnClick(callback)
  :no-index:

  Runs when any item is chosen.

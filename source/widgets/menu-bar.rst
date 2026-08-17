Menubar
###########

The strip of menus along the top of a window.

.. code-block:: lua
  :linenos:

  local ui = require("limekit.ui")

  local menubar = ui.Menubar()

  local file = ui.Menu("File")
  file:addMenuItem(ui.MenuItem("New"))
  file:addMenuItem(ui.MenuItem("Open"))

  local help = ui.Menu("Help")
  help:addMenuItem(ui.MenuItem("About"))

  menubar:addMenu(file)
  menubar:addMenu(help)

  window:setMenubar(menubar)

.. important::

  A menubar only appears once you attach it to a window with
  ``window:setMenubar(menubar)``.

Contents
***************

.. function:: addMenu(menu)
  :no-index:

  Adds a :doc:`Menu </widgets/menu>` to the bar.

.. function:: addMenuItem(item)
  :no-index:

  Adds a single command directly to the bar, without a menu around it.

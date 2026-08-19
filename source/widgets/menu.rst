Menu
###########

A menu of commands. Menus hold :doc:`MenuItems </widget-items/menu-item>`, other
menus (which become submenus), and separators.

.. code-block:: lua
  :linenos:

  local ui = require("limekit.ui")

  local file = ui.Menu("File")

  local open = ui.MenuItem("Open")
  open:setShortcut("Ctrl+O")
  open:setOnClick(function()
      openDocument()
  end)

  local quit = ui.MenuItem("Quit")
  quit:setOnClick(function()
      sys.System.exit()
  end)

  file:addMenuItem(open)
  file:addSeparator()
  file:addMenuItem(quit)

A menu on its own does nothing -- put it somewhere:

* on a :doc:`Menubar </widgets/menu-bar>` at the top of the window
* on a :doc:`Button </widgets/button>` with ``setMenu``
* on a :doc:`SysTray </batteries>` icon
* wherever the user right-clicked, with ``popupAt``

.. note::

  1.x had ``buildFromTemplate`` and ``fromTemplate`` for building a menu from a
  table. There were three inconsistent versions of it and all of them ended up
  calling ``addMenuItem`` anyway, so they are gone. Build menus with
  ``addMenuItem`` and ``addMenu``.

Contents
***************

.. function:: addMenuItem(item)
  :no-index:

  Adds a command.

.. function:: addMenu(menu)
  :no-index:

  Adds another menu as a submenu.

  .. code-block:: lua

     local recent = ui.Menu("Open recent")
     recent:addMenuItem(ui.MenuItem("report.pdf"))
     file:addMenu(recent)

.. function:: addSeparator()
  :no-index:

  Adds a dividing line to group related commands.

Showing it
***************

.. function:: popupAt(widget, x, y)
  :no-index:

  Shows the menu at ``x``, ``y`` measured from ``widget``'s top-left corner --
  which is exactly the pair a ``setOnContextMenu`` handler receives, so the two
  fit together directly.

  .. code-block:: lua

     window:setOnContextMenu(function(sender, x, y)
         local menu = ui.Menu()
         menu:addMenuItem(ui.MenuItem("Cut"))
         menu:addMenuItem(ui.MenuItem("Copy"))
         menu:popupAt(sender, x, y)
     end)

  Building the menu inside the handler, rather than once up front, lets the
  entries depend on what was actually clicked.

Appearance
***************

.. function:: setTitle(text) / getTitle()
  :no-index:

  The menu's name, as shown on the menubar.

.. function:: setIcon(path) / getIcon()
  :no-index:

  An icon beside the name.

Events
***************

.. function:: setOnClick(callback)
  :no-index:

  Runs when any item in the menu is chosen. Individual items can have their own
  handlers too.

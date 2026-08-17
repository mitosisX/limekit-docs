Window
###########

The window is the frame your application lives in. Every app needs one, and it
is usually the first thing you create.

.. code-block:: lua

  local ui = require("limekit.ui")

  local window = ui.Window { title = "My app", size = { 640, 480 } }
  window:show()

The options table is the tidiest way to set several things at once. Every key
is optional -- a bare ``ui.Window()`` gives you a 400x400 window titled
"Limekit".

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Key
     - Meaning
   * - ``title``
     - The text in the title bar
   * - ``size``
     - A ``{width, height}`` pair
   * - ``location``
     - An ``{x, y}`` pair placing the window on screen
   * - ``icon``
     - The window icon, usually from ``res.Resources.images(...)``

.. important::

  A window shows nothing until you give it a layout and call ``show()``.

  .. code-block:: lua

     local layout = ui.VLayout()
     layout:addChild(ui.Label("Hello"))

     window:setLayout(layout)
     window:show()

Contents
***************

.. function:: setLayout(layout)
  :no-index:

  Puts a layout in the window. This is how nearly every app fills its window.

.. function:: setMainChild(child)
  :no-index:

  Puts a single widget in the window instead of a layout. Useful when the whole
  window is one thing, such as a :doc:`Tab </widgets/tab>` or a
  :doc:`Scroller </widgets/scroller>`.

.. function:: setMenubar(menubar)
  :no-index:

  Attaches a :doc:`Menubar </widgets/menu-bar>` along the top.

.. function:: addToolbar(toolbar, position)
  :no-index:

  Adds a :doc:`Toolbar </widgets/tool-bar>`. ``position`` is ``top``,
  ``bottom``, ``left`` or ``right`` and defaults to ``top``.

.. function:: addDockable(dock, area)
  :no-index:

  Adds a :doc:`Dock </widgets/dock>` panel. ``area`` is ``left``, ``right``,
  ``top`` or ``bottom`` and defaults to ``left``.

Appearance
***************

.. function:: setTitle(text) / getTitle()
  :no-index:

  The text in the title bar.

.. function:: setIcon(path) / getIcon()
  :no-index:

  The window icon.

  .. code-block:: lua

     local res = require("limekit.res")
     window:setIcon(res.Resources.images("app.png"))

.. function:: setCustomCursor(cursor)
  :no-index:

  The mouse cursor shown over the window. Accepts names like ``arrow``,
  ``wait``, ``ibeam``, ``cross``, ``pointinghand``, ``openhand``, ``forbidden``.

Position and size
*******************

.. function:: getSize()
  :no-index:

  The current ``{width, height}`` of the window.

.. function:: center()
  :no-index:

  Moves the window to the middle of the screen.

  .. note::

     Limekit centres a window automatically the first time it is shown. If the
     user then moves it, re-showing the window leaves it where they put it.

.. function:: maximize()
  :no-index:

  Fills the screen.

.. function:: minimize()
  :no-index:

  Sends the window to the taskbar.

.. function:: setAlwaysOnTop(ontop)
  :no-index:

  Keeps the window above other windows.

Events
***************

.. function:: setOnShown(callback)
  :no-index:

  Runs when the window is first shown.

.. function:: setOnClose(callback)
  :no-index:

  Runs when the user closes the window.

.. function:: setOnResize(callback)
  :no-index:

  Runs when the window is resized. The handler receives the window, the new
  width and the new height.

  .. code-block:: lua

     window:setOnResize(function(sender, width, height)
         print(width .. "x" .. height)
     end)

.. function:: setOnMouseMove(callback)
  :no-index:

  Runs as the pointer moves over the window. Receives the window, ``x`` and ``y``.

.. function:: setOnMousePress(callback)
  :no-index:

  Runs when a mouse button goes down. Receives the window, ``x`` and ``y``.

.. function:: setOnMouseRelease(callback)
  :no-index:

  Runs when a mouse button comes back up. Receives the window, ``x`` and ``y``.

.. function:: setOnMouseDoubleClick(callback)
  :no-index:

  Runs on a double click. Receives the window, ``x`` and ``y``.

.. function:: setOnContextMenu(callback)
  :no-index:

  Runs on a right click. Receives the window, ``x`` and ``y``.

  .. code-block:: lua

     window:setOnContextMenu(function(sender, x, y)
         print("right clicked at " .. x .. ", " .. y)
     end)

Window
=========

This is the fundamental widgets that serves as the main window of any application. It provies a framework for building the main user interface of an application, typically containing menu bars, toolbars, and a layout where other widgets are placed.

.. code-block:: lua

  local window = Window{title = 'Limekit', icon = images('app.png'), size={200,200}}
  window:show()

Properties
***************

.. function:: setOnShown(callback)
  
  Executed whenever the window is shown or displayed on the screen.

.. function:: setOnClose(callback)
  
  Executed when the window is closing.
  
.. function:: setOnResize(callback)
  
  Executed whenever the window is being resized.

.. function:: maximize()

  Used to enlarge a window to fill the entire screen. It allows the window to occupy the maximum available space on the screen

.. function:: minimize()
  
  Minimizes or iconifies a window to the system taskbar or dock. It shrinks the window and places an icon representing the window in the taskbar or dock, allowing users to easily restore the window later

.. function:: setMinSize(width, height)

  Sets the minimum size

.. function:: setMaxHeight(height)

  Sets the maximum height

.. function:: setMinHeight(height)

  Sets the minimum height

.. function:: setMaxWidth(width)

  Sets the maximum width

.. function:: setMinWidth(width)

  Sets the minimum width

.. function:: setMaxSize(width, height)

  Sets the maximum size

.. function:: setCustomCursor(path)

  Sets a custom cursor icon from path for the window

.. function:: setTitle(title)

  Sets the title for the window

.. function:: setMainWidget(widget)

  Sets any widget as the central widget, causing it to take up the available space.

.. function:: setSize(width, height)

  Sets the size of the window

.. function:: setLayout(layout)

  Sets a primary layout for the window

.. function:: addDock(dock, area: optional)

  Adds a dock to the window.

  Areas available: ``left``, ``right``, ``top``, ``bottom``, ``allareas`` and ``nodock``

checkout :doc:`Docks </widgets/dock>`

.. function:: setIcon(path)

  Sets the icon for the window

.. function:: addToolbar(toolbar)

  Adds a toolbar to the window
  
checkout :doc:`Tool bars </widgets/tool-bar>`

.. function:: setMenubar(menubar)

  Sets a menubar for the window

checkout :doc:`Menu bars </widgets/menu-bar>`

.. note::

  There can only be one menubar per window

.. function:: center()

  Centers the window

.. function:: setFixedSize(width, height)

  Sets a fixed size to restrict resizing the window

.. function:: show()

  Shows the window
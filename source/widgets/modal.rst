Modal
===========

A window that pops up to interact with users, often for specific tasks or information gathering. It's a specialized window used to prompt users for input, display information, or perform actions that require user interaction.

.. code-block:: lua

  local modal = Modal(window, title)
  modal:show()

.. note::

  You can only set one primary layout for each modal

Properties
***************

.. function:: setOnShown(callback)
  
  Executed whenever the window is shown or displayed on the screen.

.. function:: setOnClose(callback)
  
  Executed when the window is closing.

  :params: ``self`` and ``event``: use :mod:`ignore()` and :mod:`accept()` on ``event``; ``event.ignore()`` or ``event.accept()``
  
.. function:: setOnResize(callback)
  
  Executed whenever the window is being resized.

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

.. function:: setTitle(title)

  Sets the title for the window

.. function:: setMainWidget(widget)

  Sets any widget as the central widget, causing it to take up the available space.

.. function:: setSize(width, height)

  Sets the size of the window

.. function:: setLayout(layout)

  Sets a primary layout for the window

.. function:: setIcon(path)

  Sets the icon for the window

.. function:: setFixedSize(width, height)

  Sets a fixed size to restrict resizing the window

.. function:: show()

  Shows the window

.. function:: dismiss()

  Closes the modal
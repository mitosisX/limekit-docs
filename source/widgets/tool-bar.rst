ToolBar
===========

A movable panel that contains various interactive elements like buttons, tool buttons, text fields, or other widgets. It's commonly used to provide quick access to frequently used actions or tools within an application.

.. code-block:: lua

  local toolbar = Toolbar()

.. admonition:: Hey!

  Check out :doc:`ToolbarButton </widget-items/toolbar-item>` for more

Properties
***************

.. function:: setIconStyle(style)

  Sets the toolbar icon style; ``icononly``, ``textonly``, ``textbesideicon``, ``textundericon``, ``followstyle``

.. function:: setIconSize(width, height)
  :noindex:

  Adjusts the icon size for all :mod:`ToolbarButton`

.. function:: addButton(data, startNode, endNode)

  Adds a :mod:`ToolbarButton` to the widget
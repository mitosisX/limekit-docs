Dock
=======

A versatile element used to create dockable panes or windows within an application's main window. These dock widgets can be moved, resized, and placed in various positions, such as docking them to the edges or floating them as separate windows. They're commonly used to provide additional panels or toolbars that users can arrange according to their preferences for a more customized user interface experience.

.. code-block:: lua

  local dock = Dock()

Methods
***************

.. function:: setProperties(properties)
  :noindex:

  Sets rules on how the dock widget behaves. Available properties include ``floatable``, ``movable``, ``closable`` and ``nil``

  :param properties: lua table 

.. function:: setMagneticAreas(areas)
  
  Sets the areas the dock widget is allowed to float to. Available areas include ``left``, ``top``, ``right``, ``bottom``, ``all`` and ``nil``

  :param areas: lua table 

.. function:: setTitle(text)
  
  Sets text displayed on the dock widget

.. function:: addChild(child)
  
  Add a widget to the widget

.. function:: setLayout(layout)
  
  Add a layout to the widget
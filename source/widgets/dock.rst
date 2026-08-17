Dock
###########

A panel attached to an edge of the window that the user can move, float as a
separate window, or close. Tool palettes and side panels are the usual use.

.. code-block:: lua
  :linenos:

  local ui = require("limekit.ui")

  local tools = ui.Dock("Tools")

  local inner = ui.VLayout()
  inner:addChild(ui.Button("Brush"))
  inner:addChild(ui.Button("Eraser"))
  tools:setLayout(inner)

  window:addDockable(tools, "left")

.. note::

  The 1.x name ``Dockable`` still works and refers to this same widget.

Contents
***************

.. function:: ui.Dock(title)
  :no-index:

  Creates a dock panel.

.. function:: setLayout(layout) / getLayout()
  :no-index:

  The layout held inside.

.. function:: setChild(child) / getChild()
  :no-index:

  A single widget inside, instead of a layout.

.. function:: setTitleBarChild(child)
  :no-index:

  Replaces the title bar with a widget of your own.

Behaviour
***************

.. function:: setAllowedAreas(...)
  :no-index:

  Which edges the panel may be docked to: ``left``, ``right``, ``top``,
  ``bottom``, ``all`` or ``none``. Pass as many as you like.

  .. code-block:: lua

     tools:setAllowedAreas("left", "right")

  .. note::

     This replaces 1.x's ``setMagneticAreas``, which silently ignored any area
     name it did not recognise. An unknown name now raises an error.

.. function:: setFeatures(...)
  :no-index:

  Which of move, float and close the user is allowed to do.

.. function:: setFloating(floating) / isFloating()
  :no-index:

  Whether the panel is detached from the window.

Appearance
***************

.. function:: setTitle(text) / getTitle()
  :no-index:

  The heading on the panel.

.. function:: setIcon(path) / getIcon()
  :no-index:

  An icon shown in the title bar.

Events
***************

.. function:: setOnLocationChange(callback)
  :no-index:

  Runs when the panel is docked to a different edge.

.. function:: setOnVisibilityChange(callback)
  :no-index:

  Runs when the panel is shown or hidden.

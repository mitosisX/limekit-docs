Splitter
###########

Divides space between two or more widgets with a bar the user can drag. Think
of a file browser beside a preview pane.

.. code-block:: lua
  :linenos:

  local ui = require("limekit.ui")

  local splitter = ui.Splitter("horizontal")
  splitter:addChild(fileList)
  splitter:addChild(preview)
  splitter:setSizes({ 200, 500 })

Properties
***************

.. function:: ui.Splitter(orientation)
  :no-index:

  Creates a splitter. ``orientation`` is ``horizontal`` or ``vertical`` and
  defaults to ``vertical``.

  .. note::

     ``horizontal`` places the panes side by side, with a vertical bar between
     them.

.. function:: addChild(child)
  :no-index:

  Adds a widget as a pane.

.. function:: addLayout(layout)
  :no-index:

  Adds a whole layout as a pane.

.. function:: setSizes(sizes)
  :no-index:

  The starting size of each pane, from a table of numbers. There should be one
  number per pane.

.. function:: getSizes()
  :no-index:

  The current pane sizes -- useful for saving a user's layout between runs.

.. function:: setOrientation(orientation) / getOrientation()
  :no-index:

  ``horizontal`` or ``vertical``.

.. function:: setHandleWidth(width) / getHandleWidth()
  :no-index:

  How thick the draggable bar is.

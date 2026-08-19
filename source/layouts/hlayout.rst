HLayout
##########

Arranges widgets in a row, left to right.

.. code-block:: lua
  :linenos:

  local ui = require("limekit.ui")

  local buttons = ui.HLayout()
  buttons:addChild(ui.Button("Cancel"))
  buttons:addChild(ui.Button("Save"))

Properties
***************

.. function:: addChild(child, stretch)
  :no-index:

  Adds a widget. ``stretch`` decides how much of any spare room this widget
  takes compared with the others; it defaults to 0, meaning "only what you
  need".

  .. code-block:: lua

     local row = ui.HLayout()
     row:addChild(ui.LineEdit(), 1)     -- takes all the spare width
     row:addChild(ui.Button("Go"))      -- stays its natural size

.. function:: addLayout(layout, stretch)
  :no-index:

  Adds a nested layout as one item in the row.

.. function:: addStretch(stretch)
  :no-index:

  Adds a springy gap that soaks up leftover space. This is how you push widgets
  to one end.

  .. code-block:: lua

     local row = ui.HLayout()
     row:addStretch(1)
     row:addChild(ui.Button("Next"))    -- pinned to the right

.. function:: addSpacing(size)
  :no-index:

  Adds a fixed gap of a given number of pixels.

.. function:: addSpacer(spacer)
  :no-index:

  Adds a :doc:`Spacer </widgets/spacer>` -- a fixed gap you can build once and
  reuse. A Spacer is a layout item rather than a widget, so ``addChild``
  rejects it and this is the method that takes one.

.. seealso::

  :doc:`VLayout </layouts/vlayout>` for a column, and
  :doc:`Layout Managers </layouts>` for the methods every layout shares.

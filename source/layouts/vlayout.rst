VLayout
##########

Arranges widgets in a column, top to bottom. This is the layout most apps start
with.

.. code-block:: lua
  :linenos:

  local ui = require("limekit.ui")

  local page = ui.VLayout()
  page:setSpacing(10)
  page:setMargins(20, 20, 20, 20)
  page:addChild(ui.Label("What's your name?"))
  page:addChild(ui.LineEdit())
  page:addChild(ui.Button("Continue"))

Properties
***************

.. function:: addChild(child, stretch)
  :no-index:

  Adds a widget. ``stretch`` decides how much of any spare height this widget
  takes compared with the others; it defaults to 0.

  .. code-block:: lua

     local page = ui.VLayout()
     page:addChild(ui.Label("Notes"))
     page:addChild(ui.TextField(), 1)   -- grows to fill the window

.. function:: addLayout(layout, stretch)
  :no-index:

  Adds a nested layout as one item in the column -- typically an
  :doc:`HLayout </layouts/hlayout>` of buttons at the bottom.

.. function:: addStretch(stretch)
  :no-index:

  Adds a springy gap that soaks up leftover height, pushing what follows to the
  bottom.

  .. code-block:: lua

     page:addStretch(1)
     page:addLayout(buttonRow)          -- pinned to the bottom

.. function:: addSpacing(size)
  :no-index:

  Adds a fixed gap of a given number of pixels.

.. function:: addSpacer(spacer)
  :no-index:

  Adds a :doc:`Spacer </widgets/spacer>` -- a fixed gap you can build once and
  reuse. A Spacer is a layout item rather than a widget, so ``addChild``
  rejects it and this is the method that takes one.

.. seealso::

  :doc:`HLayout </layouts/hlayout>` for a row, and
  :doc:`Layout Managers </layouts>` for the methods every layout shares.

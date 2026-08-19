Spacer
###########

An invisible block of a fixed size, used to push widgets apart.

.. code-block:: lua

  local ui = require("limekit.ui")

  local layout = ui.HLayout()
  layout:addChild(ui.Button("Back"))
  layout:addSpacer(ui.Spacer(40, 0))
  layout:addChild(ui.Button("Next"))

.. function:: ui.Spacer(width, height)
  :no-index:

  Creates a gap of a given size.

.. important::

  Add a Spacer with the layout's ``addSpacer``, not ``addChild``. A Spacer is
  not a widget -- it is a layout item -- so ``addChild`` rejects it.

  For a one-off gap you do not need to keep hold of, ``addSpacing(40)`` says
  the same thing in one call.

.. note::

  A Spacer is a fixed gap. When you want the gap to *absorb* whatever room is
  left over -- pushing one button to the far right, say -- use the layout's own
  ``addStretch`` instead:

  .. code-block:: lua

     local layout = ui.HLayout()
     layout:addChild(ui.Button("Back"))
     layout:addStretch(1)
     layout:addChild(ui.Button("Next"))

  See :doc:`Layout Managers </layouts>`.

HLine
###########

A horizontal dividing line. Add it to a
:doc:`VLayout </layouts/vlayout>` to separate sections of a form.

.. code-block:: lua

  local ui = require("limekit.ui")

  local layout = ui.VLayout()
  layout:addChild(ui.Label("Personal details"))
  layout:addChild(ui.LineEdit())
  layout:addChild(ui.HLine())
  layout:addChild(ui.Label("Payment"))

An HLine has no properties of its own -- it is a line. The
:doc:`common widget methods </widgets>` all apply, so you can style it:

.. code-block:: lua

  local rule = ui.HLine()
  rule:setStyleSheet("color: #ddd;")

.. seealso::

  :doc:`VLine </widgets/vline>` for a vertical line, and
  :doc:`Separator </widgets/separator>` for one where you choose the direction.

VLine
###########

A vertical dividing line. Add it to an
:doc:`HLayout </layouts/hlayout>` to separate columns.

.. code-block:: lua

  local ui = require("limekit.ui")

  local layout = ui.HLayout()
  layout:addChild(sidebar)
  layout:addChild(ui.VLine())
  layout:addChild(content)

A VLine has no properties of its own. The
:doc:`common widget methods </widgets>` all apply.

.. seealso::

  :doc:`HLine </widgets/hline>` for a horizontal line, and
  :doc:`Separator </widgets/separator>` for one where you choose the direction.

Separator
############

A dividing line, in whichever direction you ask for. It is the same idea as
:doc:`HLine </widgets/hline>` and :doc:`VLine </widgets/vline>`, with the
orientation chosen at creation time rather than by picking a different class.

.. code-block:: lua

  local ui = require("limekit.ui")

  local layout = ui.VLayout()
  layout:addChild(ui.Label("Account"))
  layout:addChild(ui.Separator("horizontal"))
  layout:addChild(ui.Label("Privacy"))

Properties
***************

.. function:: ui.Separator(orientation)
  :no-index:

  Creates a separator. ``orientation`` is ``horizontal`` or ``vertical`` and
  defaults to ``horizontal``.

  .. note::

     A ``horizontal`` separator is a horizontal line, which divides content
     stacked vertically. Reach for a ``vertical`` one inside an
     :doc:`HLayout </layouts/hlayout>`.

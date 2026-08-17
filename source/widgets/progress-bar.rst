ProgressBar
##############

Shows how far along a task is.

.. code-block:: lua

  local ui = require("limekit.ui")

  local progress = ui.ProgressBar()
  progress:setRange(0, 100)
  progress:setValue(0)

.. important::

  A progress bar only redraws when the interface is free to do so. If you
  update it inside a long loop on the main thread, the window freezes and the
  bar appears stuck. Do the slow work in a :doc:`Thread </batteries>` and update
  the bar from a :doc:`Signal </batteries>`.

Properties
***************

.. function:: setValue(value) / getValue()
  :no-index:

  How far along the task is.

.. function:: setRange(start, end_)
  :no-index:

  The values that count as empty and full.

.. function:: setOrientation(orientation) / getOrientation()
  :no-index:

  ``horizontal`` or ``vertical``.

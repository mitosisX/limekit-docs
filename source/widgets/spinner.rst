Spinner
###########

A number box with up and down arrows, for whole numbers. For decimals use a
:doc:`DoubleSpinner </widgets/double-spinner>`.

.. code-block:: lua

  local ui = require("limekit.ui")

  local quantity = ui.Spinner()
  quantity:setRange(1, 99)
  quantity:setValue(1)

Properties
***************

.. function:: setValue(value) / getValue()
  :no-index:

  The current number.

.. function:: setRange(start, end_)
  :no-index:

  The lowest and highest numbers allowed.

.. function:: setPrefix(text) / getPrefix()
  :no-index:

  Text shown before the number.

.. function:: setSuffix(text) / getSuffix()
  :no-index:

  Text shown after the number -- useful for units.

  .. code-block:: lua

     local delay = ui.Spinner()
     delay:setRange(0, 60)
     delay:setSuffix(" seconds")

.. function:: setOnValueChange(callback)
  :no-index:

  Runs whenever the number changes, whether typed or clicked.

  .. code-block:: lua

     quantity:setOnValueChange(function(sender)
         updateTotal(sender:getValue())
     end)

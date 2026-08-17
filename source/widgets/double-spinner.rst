DoubleSpinner
################

A number box for decimal values. Identical to a
:doc:`Spinner </widgets/spinner>` except that it accepts fractions.

.. code-block:: lua

  local ui = require("limekit.ui")

  local price = ui.DoubleSpinner()
  price:setRange(0, 1000)
  price:setValue(9.99)
  price:setPrefix("$ ")

Properties
***************

.. function:: setValue(value) / getValue()
  :no-index:

  The current number, as a decimal.

.. function:: setRange(start, end_)
  :no-index:

  The lowest and highest values allowed.

.. function:: setPrefix(text) / getPrefix()
  :no-index:

  Text shown before the number.

.. function:: setSuffix(text) / getSuffix()
  :no-index:

  Text shown after the number.

.. function:: setOnValueChange(callback)
  :no-index:

  Runs whenever the value changes.

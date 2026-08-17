AdvancedSlider
#################

A slider that draws itself: it fills as you drag and prints the current value
inside the bar. Use it when the slider is a feature of the interface rather
than a plain control -- audio apps, dashboards, settings panels.

.. code-block:: lua

  local ui = require("limekit.ui")

  local gain = ui.AdvancedSlider()
  gain:setRange(0, 100)
  gain:setValue(65)
  gain:setSuffix(" %")
  gain:setAccentColor("#2d7d46")

Unlike the plain :doc:`Slider </widgets/slider>`, this widget paints its own
background, so use ``setBackgroundColor`` rather than a stylesheet to change it.

Value
***************

.. function:: setValue(value) / getValue()
  :no-index:

  The current value.

.. function:: getValueFormatted()
  :no-index:

  The value as it appears on the bar, with prefix, suffix and separators
  applied.

.. function:: setRange(minimum, maximum) / getRange()
  :no-index:

  The lowest and highest values.

.. function:: setMinimum(minimum) / getMinimum()
  :no-index:

.. function:: setMaximum(maximum) / getMaximum()
  :no-index:

  The ends of the range individually.

.. function:: setFloat(use_float) / isFloat()
  :no-index:

  Whether the value is a decimal rather than a whole number.

.. function:: setDecimals(decimals) / getDecimals()
  :no-index:

  How many decimal places to show.

.. function:: setSingleStep(step) / getSingleStep()
  :no-index:

  How far one arrow-key press moves the value.

.. function:: setPageStep(step) / getPageStep()
  :no-index:

  How far Page Up and Page Down move the value.

Text
***************

.. function:: setPrefix(text) / getPrefix()
  :no-index:

  Text shown before the value.

.. function:: setSuffix(text) / getSuffix()
  :no-index:

  Text shown after the value.

.. function:: setDecimalSeparator(separator) / getDecimalSeparator()
  :no-index:

  The character used for the decimal point.

.. function:: setThousandsSeparator(separator) / getThousandsSeparator()
  :no-index:

  The character used to group thousands.

.. function:: showValue(on) / isShowingValue()
  :no-index:

  Whether the value is printed on the bar at all.

.. function:: setValuePosition(position) / getValuePosition()
  :no-index:

  Where on the bar the value is printed.

.. function:: setFont(font) / getFont()
  :no-index:

  The font used for the value.

Appearance
***************

.. function:: setAccentColor(colour) / getAccentColor()
  :no-index:

  The colour of the filled portion.

.. function:: setBackgroundColor(colour) / getBackgroundColor()
  :no-index:

  The colour of the unfilled portion.

.. function:: setTextColor(colour) / getTextColor()
  :no-index:

  The colour of the printed value.

.. function:: setBorderColor(colour) / getBorderColor()
  :no-index:

  The colour of the outline.

.. function:: setBorderRadius(radius) / getBorderRadius()
  :no-index:

  How rounded the corners are.

Input
***************

.. function:: setKeyboardInputEnabled(enabled) / isKeyboardInputEnabled()
  :no-index:

  Whether arrow keys change the value.

.. function:: setMouseWheelInputEnabled(enabled) / isMouseWheelInputEnabled()
  :no-index:

  Whether the scroll wheel changes the value.

Events
***************

.. function:: setOnValueChanged(callback)
  :no-index:

  Runs whenever the value changes.

RadioButton
=============

This functions as a button that allows toggling between being selected (checked) or deselected (unchecked). Generally, these buttons offer users a choice among several options where only one can be selected at a time. Within a set of radio buttons, selecting a new option automatically deselects the previously chosen one.

Properties
***************

.. code-block:: lua

  local check = RadioButton(text)

.. function:: setOnCheck(callback)

  Executed when checked. Arguments passed include self and state.

.. function:: setIcon(path)

  Sets an icon on the radio button

checkout :doc:`Using resources </widgets/accordion>`

.. function:: setIconSize(width, height)
  
  Sets the icon size

.. function:: setTooltip(text)

  Tooltips are brief informational messages that appear when the user hovers the mouse pointer over the tab

.. function:: setTooltipDuration(duration)

  Set how long the tooltip displays

.. function:: getTooltip()

  Returns the tooltip text

.. function:: getCheck()

  Returns check status; ``true`` or ``false``

.. function:: setCheck(check: bool)

  Sets the box to be checked or not

.. function:: setText(text)

  Sets the radio button text

.. function:: getText()

  Gets the radio button button
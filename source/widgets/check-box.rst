CheckBox
=============

A small box that can be checked or unchecked by users. It's used to toggle something on or off in an application, like enabling or disabling a feature or selecting options.

.. code-block:: lua

  local check = CheckBox(text)

Properties
***************

.. function:: setOnCheck(callback)
  :noindex:

  Executed when checked. Arguments passed include self and state.

.. function:: setIcon(path)

  Sets an icon on the check box

checkout :doc:`Using resources </user-resources>`

.. function:: setIconSize(width, height)
  
  Sets the icon size

.. function:: setToolTip(text)

  Tooltips are brief informational messages that appear when the user hovers the mouse pointer over the tab
  
.. function:: getTooltip()

  Returns the tooltip text

.. function:: setToolTipDuration(check: bool)

  Set how long the tooltip displays

.. function:: getCheck()

  Returns check status; true or false

.. function:: setCheck(check: bool)

  Sets the box to be checked or not

.. function:: setText(text)

  Sets the check box text

.. function:: getText()

  Gets the check box button

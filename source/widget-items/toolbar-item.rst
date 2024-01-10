ToolbarButton
=============

A widget/button that can only be used in a :mod:`Toolbar`

.. code-block:: lua

  -- setting the title to - (dash) treats it as a separator
  local homepage = ToolbarButton(title: optional)

Properties
***************

.. function:: setOnClick(callback)
  :noindex:

  The function executed when the button is clicked

.. function:: setText(text)
  :noindex:
  
  Sets the text on the button

.. function:: setIcon(path)
  :noindex:

  Sets an icon on the button

.. function:: setToolTip(tooltip)
  
  Sets the tooltip for the button

.. function:: setMenu(menu)
  :noindex:

  Sets a menu for the button

.. function:: setCheckable(checkable: bool)

  Allows the button to be checkable or to be toggled

.. function:: isChecked()
  :noindex:

  Checks if the button is checked/toggles

.. function:: setChecked(check: bool)

  Checks/toggles the button

.. function:: setVisibility(visible: bool)
  :noindex:

  Sets the visibility for the button

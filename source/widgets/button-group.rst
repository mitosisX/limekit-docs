ButtonGroup
=============

This widgets helps you manage a group of :doc:`check boxes </widgets/check-box>` or :doc:`radio buttons </widgets/check-box>`, making sure that only one can be selected at a time. It simplifies handling od multiple buttons by letting you know which one's clicked or selected within the group.

.. code-block:: lua

  local group = GroupBox()

You can add buttons (radio button and check box) to the widget using the ``addButton(button)``

.. code-block:: lua

  local maleButton = RadioButton('Male')
  local femaleButton = RadioButton('Female')

  group:addButton(maleButton)
  group:addButton(femaleButton)

Methods
***************

.. function:: addChild(widget, label, icon: optional)
  
  Adds a widget in a tab to the accordion with given a label, and icon if necessary

.. function:: addLayout(layout, label, icon: optional)
  
  Adds a layout in a tab to the accordion with given a label, and icon if necessary

checkout :doc:`Using resources </widgets/accordion>`

.. function:: setTooltip(text)

  Enable text that appears when a mouse hovers on the tab

.. function:: getCurrentIndex()

  Gets the current index of the visible tab

.. function:: setCurrentIndex(index)

  Sets the index of the tab to be visible

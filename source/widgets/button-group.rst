ButtonGroup
=============

This widgets helps you manage a group of :doc:`check boxes </widgets/check-box>` or :doc:`radio buttons </widgets/check-box>`, making sure that only one can be selected at a time. It simplifies handling of multiple buttons by letting you know which one's clicked or selected within the group.

.. code-block:: lua

  local group = GroupBox()

You can add buttons (radio button and check box) to the widget using the ``addButton(button)``

.. code-block:: lua

  local maleButton = RadioButton('Male')
  local femaleButton = RadioButton('Female')

  group:addButton(maleButton)
  group:addButton(femaleButton)

.. important::
  Don not add the ``ButtonGroup`` to any layout. First, add the button to the ``ButtonGroup``. After that, add the button to any layout you prefer, as shown below.

.. code-block:: lua

  local boolean = RadioButton('True')

  group:addButton(boolean)
  layout:addChild(boolean)

Properties
***************

.. function:: addChild(widget, label, icon: optional)
  
  Adds a widget in a tab to the accordion with a given label, and an icon if necessary

.. function:: addLayout(layout, label, icon: optional)
  
  Adds a layout in a tab to the accordion with a given label, and an icon if necessary

checkout :doc:`Using resources </user-resources>`

.. function:: setTooltip(text)

  Tooltips are brief informational messages that appear when the user hovers the mouse pointer over the tab

.. function:: getCurrentIndex()

  Gets the current index of the visible tab

.. function:: setCurrentIndex(index)

  Sets the index of the tab to be visible

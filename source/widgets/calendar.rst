Calendar
###########

A powerful component designed to manage and display multiple tabs, each hosting distinct set of widgets or layouts.

.. code-block:: lua

  local accoridon = Accordion()

You can add add a widget or a layout to the accordion using ``addChild(widget, label, icon: optional)`` or ``addLayout(layout, label, icon: optional)``, respectively. Take a look at the different code snippet below

*Adding a widget*

.. code-block:: lua

  local button = Button('Click me')
  accordion:addChild(button, 'All Buttons')

  -- or otherwise with an icon

  local button = Button('Click me')
  accordion:addChild(button, 'All Buttons', images('icon.png'))

*Adding a layout*

.. code-block:: lua

  local layout = VLayout()
  local button = Button('Click me')

  layout:addChild(button)
  accordion:addChild(layout, 'All Buttons')

  -- or otherwise with an icon

  local layout = VLayout()
  local button = Button('Click me')

  layout:addChild(button)
  accordion:addChild(layout, 'All Buttons')

*checkout* :doc:`Layout Managers </layouts>`

Properties
***************

.. function:: addChild(widget, label, icon: optional)
  
  Adds a widget in a tab to the accordion with given a label, and icon if necessary

.. function:: addLayout(layout, label, icon: optional)
  
  Adds a layout in a tab to the accordion with given a label, and icon if necessary

checkout :doc:`Using resources </user-resources>`

.. function:: setGridVisible(visible: bool)

  Show or hide grid lines on the calendar

.. function:: setTooltip(text)

  Enable text that appears when a mouse hovers on the tab

.. function:: getCurrentIndex()

  Gets the current index of the visible tab

.. function:: setCurrentIndex(index)

  Sets the index of the tab to be visible

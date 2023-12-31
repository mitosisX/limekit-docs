ComboBox
=============

A widget that presents a dropdown list of predefined options for users to select from. It's commonly used to offer users a range of choices from a list of items or categories within an application. Users can select one option from the list.

.. code-block:: lua

  local fruits = ComboBox(data: table)

  -- or like

  local fruits = ComboBox({'tomato', 'apple', 'pear', 'cherry'})

Properties
***************

.. function:: setOnItemSelected(callback)

  Executed when an item is selected from the list.

.. function:: getText()

  Gets selected item text

.. function:: addImageItem(data: table)
  
  Add an item with an icon alongside it. Use the following format: ``{'limekit', images('lua.png')}``

.. function:: addImageItems(data: table)

  Same as above method, only acceptng build data. Use the following format: ``{{'limekit', images('lua.png')}, {'apple', images('icon.png')}, ...}``

.. function:: addItem(text)

  Adds a single item to the widget

.. function:: setItems(data: table)

  Sets data to the widget. Use the following format: ``{'item 1',' item 2', 'item 3', ...}``
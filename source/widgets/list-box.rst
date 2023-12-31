ListBox
===========

A widget used to display a list of items. It allows users to view a collection of items arranged in a list format within an application. Each item in the list can contain text and/or icons. This widget provides functionalities to add, remove, select, and manipulate items in the list, making it a versatile tool for presenting and managing lists of information or options in an interface.

.. code-block:: lua

  local list = ListBox(data: optional)

Properties
***************

.. function:: setOnItemSelect(callback)

  The function when an item is selected
  
  :params: ``self``, ``text`` and ``index``

.. function:: setItemViewMode(callback)

  Sets how items are displayed in the widget: Avaibale options: ``icons`` and ``list``

.. function:: setItems(data: table)

  Sets data to the widget. Use the following format: ``{'item 1',' item 2', 'item 3', ...}``

.. function:: addImageItem(data: table)
  
  Add an item with an icon alongside it. Use the following format: ``{'limekit', images('lua.png')}``

.. function:: addImageItems(data: table)

  Same as above method, only acceptng build data. Use the following format: ``{{'limekit', images('lua.png')}, {'apple', images('icon.png')}, ...}``

.. function:: addItem(text)

  Adds a single item to the widget

.. function:: removeItem(row)

  Adds a single item to the widget

.. function:: getCurrentRow(text)

  Returns row of selected item
  
.. function:: getText()

  Returns selecte item's text

.. function:: getinsertItemAtText(row, text)

  Inserts an item at a specified row

.. function:: setAltRowColors()

  Sets alternating colors to the rows

.. function:: setIconSizes(width, height)

  Sets icons to a specified sizes

.. function:: getTextAt(row)

  Gets text at a specified row

.. function:: getItemsCount()
  
  Returns total items available
  
.. function:: clear()

  Removes all item in the list

.. function:: setAllowDragDrop(enable: bool)

  Enables or disables dragging and dropping of items

.. function:: setEnableDrag(enable: bool)

  Enables or disables drag
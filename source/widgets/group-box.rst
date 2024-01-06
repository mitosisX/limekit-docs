GroupBox
===========

A container that groups and organizes related widgets together. It provides a visual frame or box around the grouped widgets, along with an optional title, making it easier for users to understand the relationship between these widgets. It helps in structuring and presenting parts of a user interface, keeping elements organized and visually connected within an application

.. code-block:: lua

  local group = GroupBox(title: optional)

.. important::

  You can only set a layout to the widget and not add widgets directly

.. note::

  using ``setChecked(false)`` disables all the widgets in the widget. However, this only applies once ``setCheckable(true)`` has been used.


Properties
***************

.. function:: setLayout(layout)
  :noindex:

  Set a primary layout for the widget

.. function:: setBackgroundColor(color)

  Sets background color for the widget

.. function:: setTitle(title)

  Sets the title for the widget

.. function:: setToolTip(text)

  Tooltips are brief informational messages that appear when the user hovers the mouse pointer over the tab

.. function:: setToolTipDuration(duration)

  Set how long the tooltip displays

.. function:: getTooltip()

  Returns the tooltip text

.. function:: getCheck()

  Returns check status; ``true`` or ``false``

.. function:: setCheck(check: bool)

  Sets the box to be checked or not

.. function:: getTitle()

  Gets the title for the widget